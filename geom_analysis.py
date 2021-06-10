import os 
import numpy
import argparse

def calculate_distance(coords1, coords2):
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(atom_distance, min_length=0, max_length=1.5):
    """
    Checks if a distance is a bond based on a minimum and a maximum
    Inputs: distance, minimum length for bond, maximum length for bond
    Default: minimum: 0 angstroms, maimum: 1.5 angstroms
    """
    if atom_distance > min_length and atom_distance < max_length:
        return True
    else: 
        return False
    
def open_xyz(filename):
    """
    This function opens a standard xyz file.
    It returns the symbols as string and the coordinates as floats.
    """
    data = numpy.genfromtxt(fname=filename, dtype='unicode', skip_header=2)
    atom = data[:,0]
    coord = data[:,1:]
    coord = coord.astype(float)
    return atom, coord

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script analyzes a use given xyz file and outputs the lengths of all the bonds.")
    parser.add_argument('xyz_file', help='The filepath of the xyz file to analyze.')
    parser.add_argument('max_bond_distance', help='The maximum distance between atoms that is considered a bond.')
    args = parser.parse_args()
    file_location = args.xyz_file()
    atom, coord = open_xyz(file_location)
    num_atoms = len(atom)
    for i in range(0,num_atoms):
        for j in range(0,num_atoms):
            if i < j:
                distance = calculate_distance(coord[i],coord[j])
                if bond_check(distance, max_length=args.max_bond_distance) is True:
                    print(F'{atom[i]} to {atom[j]} : {distance:.3f}')
