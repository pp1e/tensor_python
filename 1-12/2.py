with open('Input.txt','r') as input_file:
    c_max=int(input_file.readline()) // 2
    h_max=int(input_file.readline()) // 6
    o_max=int(input_file.readline())

    molecule_max = c_max
    if (molecule_max > h_max):
        molecule_max = h_max
    if (molecule_max > o_max):
        molecule_max = o_max

    print('Maximum molecules count:' + str(molecule_max))   

with open('Output.txt','w') as output_file:
    output_file.write(str(molecule_max))   