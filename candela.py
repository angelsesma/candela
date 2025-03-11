import os
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt
from sgfmill import sgf, boards

# Base de datos de patrones
pattern_database = defaultdict(int)  # Tracks frequency of patterns across moves
pattern_file_counter = defaultdict(set)  # Tracks which files contain each pattern

# Counter for successfully parsed SGF files
successfully_parsed_files = 0

# List to store the number of moves per game
moves_per_game = []

def parse_sgf_file(file_path):
    """Parse an SGF file and return the game."""
    global successfully_parsed_files
    try:
        with open(file_path, "rb") as f:
            sgf_src = f.read()
        if not sgf_src:
            print(f"Error: El archivo {file_path} está vacío.")
            return None
        game = sgf.Sgf_game.from_bytes(sgf_src)
        print(f"Archivo SGF leído correctamente: {file_path}")
        successfully_parsed_files += 1  # Increment counter
        return game
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
        return None
    except ValueError as e:
        print(f"Error al leer el archivo SGF: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado al leer el archivo SGF: {e}")
        return None

def rotate_region(region):
    """Rotate the 5x5 region 90 degrees clockwise."""
    return tuple(zip(*region[::-1]))

def flip_region(region):
    """Flip the 5x5 region horizontally."""
    return tuple(tuple(row[::-1]) for row in region)

def invert_region(region):
    """Invert the 5x5 region by swapping 'b' and 'w'."""
    return tuple(tuple('b' if cell == 'w' else 'w' if cell == 'b' else cell for cell in row) for row in region)

def canonical_form(region, move):
    """Convert the 5x5 region into its canonical form by rotating, flipping, and inverting."""
    x, y = move  # Coordinates of the center of the 5x5 region

    # Replace None with appropriate symbols
    new_region = []
    for i in range(5):
        row = []
        for j in range(5):
            cell = region[i][j]
            if cell is None:
                # Check if the cell is in the first line (top edge)
                if x + i - 2 == 0:  # First line of the board
                    row.append('/')  # Use '*' for the first line
                elif x + i - 2 == 18:
                     row.append('/')  # Use '*' for the first line
                
                elif y + j - 2 == 0:
                     row.append('/')  # Use '*' for the first line
                
                elif y + j - 2 == 18:
                     row.append('/')  # Use '*' for the first line
                 # Check if the cell is within the board (lines 2 to 18) both axis
                elif 1 <= x + i - 2 < 18 and 1 <= y + j - 2 < 18:
                    row.append('+')  # Use '+' for empty cells within the board
                else:
                    row.append('.')  # Use '.' for cells outside the board
            else:
                row.append(cell)  # Keep the original cell value
        new_region.append(tuple(row))
    new_region = tuple(new_region)

    # Generate all possible transformations (rotations, flips, and inversions)
    transformations = [new_region]
    for _ in range(3):  # Rotate 90, 180, 270 degrees
        transformations.append(rotate_region(transformations[-1]))
    transformations.append(flip_region(new_region))  # Flip horizontally
    for _ in range(3):  # Rotate flipped region 90, 180, 270 degrees
        transformations.append(rotate_region(transformations[-1]))

    # Generate inversions of all transformations
    inverted_transformations = [invert_region(t) for t in transformations]
    transformations.extend(inverted_transformations)

    # Select the lexicographically smallest transformation
    canonical = min(transformations)
    return canonical

def obtain_5_by_5_region_centered_by(board, move):
    """Obtiene una región de 5x5 centrada en el movimiento dado."""
    x, y = move
    region = [[board.get(x+i, y+j) if 0 <= x+i < board.side and 0 <= y+j < board.side else None for j in range(-2, 3)] for i in range(-2, 3)]
    return tuple(map(tuple, region))  # Convertir región a tupla para usarla como clave

def process_game_records(game, file_path):
    """Procesa los registros de juegos y actualiza la base de datos de patrones."""
    board = boards.Board(19)
    moves = game.get_main_sequence()

    # Track the number of moves in this game
    num_moves = len([node for node in moves if node.get_move()[1] is not None])
    moves_per_game.append(num_moves)

    # Track patterns found in this file
    patterns_in_file = set()

    for node in moves:
        colour, move = node.get_move()
        if move is None:
            continue
        x, y = move
        board.play(x, y, colour)
        region = obtain_5_by_5_region_centered_by(board, (x, y))
        canonical_region = canonical_form(region, (x, y))  # Pasar las coordenadas del movimiento
        pattern_database[canonical_region] += 1  # Update the pattern frequency
        patterns_in_file.add(canonical_region)  # Track this pattern in the current file

    # Update the file counter for each pattern found in this file
    for pattern in patterns_in_file:
        pattern_file_counter[pattern].add(file_path)

def process_sgf_folder(folder_path, output_file):
    """Procesa todos los archivos SGF en la carpeta especificada."""
    global successfully_parsed_files
    folder_path = Path(folder_path)
    if not folder_path.exists():
        print(f"Error: La carpeta {folder_path} no existe.")
        return

    for file_path in folder_path.glob("*.sgf"):
        print(f"Procesando archivo: {file_path}")
        game = parse_sgf_file(file_path)
        if game:
            process_game_records(game, file_path)
        else:
            print(f"No se pudo procesar el archivo: {file_path}")

    # Write the pattern database to the output file, sorted by overall frequency
    with open(output_file, 'w') as f:
        # Sort patterns by frequency (descending order)
        sorted_patterns = sorted(pattern_database.keys(), key=lambda p: -pattern_database[p])

        for pattern in sorted_patterns[:20]:
            pattern_str = '\n'.join([''.join(['☻' if cell == 'b' else '☺' if cell == 'w' else cell for cell in row]) for row in pattern])
            overall_frequency = pattern_database[pattern]  # Total frequency of this pattern
            file_count = len(pattern_file_counter[pattern])  # Number of files containing this pattern
            f.write(f"\n{pattern_str}\n\n {overall_frequency} veces en {file_count} partidas \n\n\n")

    # Generate a graph for the distribution of total moves per game
    plt.hist(moves_per_game, bins=20, color='blue', edgecolor='black')
    plt.title('Distribution of Total Moves per Game')
    plt.xlabel('Number of Moves')
    plt.ylabel('Number of Games')
    graph_path = Path(folder_path) / 'moves_distribution.png'
    plt.savefig(graph_path)
    plt.close()

    # Add a reference to the graph in the output file
    with open(output_file, 'a') as f:
        f.write(f"\nGraph showing the distribution of total moves per game saved at: {graph_path}\n")

    # Print the number of successfully parsed files
    print(f"Total de archivos SGF procesados exitosamente: {successfully_parsed_files}")

def main():
    folder_path = "/sgf_files"  # Ruta relativa a la carpeta de archivos SGF
    output_file = "/output.txt"  # Ruta relativa al archivo de salida
    process_sgf_folder(folder_path, output_file)

if __name__ == "__main__":
    main()