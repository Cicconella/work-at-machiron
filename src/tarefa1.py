#!/usr/bin/python

import pydicom
import sys
import os

def get_dicom_info(filename='dicoms/0fjeqffgptvghl67enh9768ja0gr1cxa/000000.dcm'):
    # - ID, idade e sexo do paciente
    # - Accession number(ID do exame), data do exame e espaçamento dos slices.
    print_str = ""
    try:

        ds = pydicom.dcmread(filename)
        ds.dir()
    except FileNotFoundError as fnfe:
        print(f"{fnfe}\nNão foi possível abrir o arquivo: {filename}")
        pass
    else:
        try:
            # ID
            print_str += f"\nID: {ds['PatientID'].value}\n"
        except KeyError as ke:
            print(f"Campo {ke} não encontrado no arquivo {filename}")
            pass
        try:
            # IDADE
            print_str += f"\nIdade: {int(ds['PatientAge'].value[0:3])} anos\n"
        except KeyError as ke:
            print(ke)
            pass
        try:
            # converte de letra do genero para a palavra completa
            id_sex = ds['PatientSex'].value
        except KeyError as ke:
            print(ke)
            pass
        else:
            if id_sex == 'F':
                sexo = 'Feminino'
            else:
                sexo = 'Masculino'
            print_str += f"\nSexo: {sexo}\n"
        try:
            print_str += f"\nID do exame: {ds['AccessionNumber'].value}\n"
        except KeyError as ke:
            print(ke)
            pass
        try:
            data = ds['AcquisitionDate'].value
        except KeyError as ke:
            print(ke)
            pass
        else:
            # converte do formato aaaammdd para dd/mm/aaaa
            ano = data[0:4]
            mes = data[4:6]
            dia = data[6:8]
            print_str += f"\nData da aquisição: {dia}/{mes}/{ano}\n"
        try:
            print_str += f"\nEspaçamento dos slices: {ds['SliceThickness'].value} mm\n"
        except KeyError as ke:
            print(ke)
            pass
    print(print_str)


def main(argv):
    if len(argv) == 3 and argv[1] == '-i':
        get_dicom_info(argv[2])
    else:
        print(f"Uso: {os.path.basename(argv[0])} -i \"caminho_para_imagem_dicom\"")


if __name__ == "__main__":
    main(sys.argv)
