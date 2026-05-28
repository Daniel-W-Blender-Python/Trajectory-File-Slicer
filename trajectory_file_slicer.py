import argparse

def slice_dat_file(file_path, output_path, start_time, end_time):
    with open(file_path, 'r') as file, open(output_path, 'w') as out_file:
        time_dict = {}
        line_num = 0

        stream_output = False
        
        for line in file:
            if line.startswith('t'):
                current_time = line.split('=')[1].strip()

                if int(current_time) == start_time:
                    stream_output = True
                elif int(current_time) == end_time:
                    stream_output = False

            if stream_output:
                out_file.write(line)

        print("Trajectory file sliced.")


# test: slice_dat_file('C:/Users/dgwill/Downloads/slice.dat', 'C:/Users/dgwill/Downloads/slice_sliced.dat', 427000000, 435500000)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Slice a trajectory file between timestamps."
    )
    
    parser.add_argument("input", help="Path to the input .dat trajectory file")
    parser.add_argument("output", help="Path to the output .dat file")
    parser.add_argument("start", type=int, help="The start timestamp (integer)")
    parser.add_argument("end", type=int, help="The end timestamp (integer)")
    
    args = parser.parse_args()
    
    slice_dat_file(args.input, args.output, args.start, args.end)
