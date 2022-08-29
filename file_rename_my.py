import os

folder = r'D:\[CG_2.0\render_\props\fossil\iguanadon\turnaround\\'

count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name
    if count<10:
    # Adding the count to the new file name and extension
        destination = folder + "shot_" + "0" +  str(count) + ".jpg"
    else:
        destination = folder + "shot_" + str(count) + ".jpg"

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
# verify the result

res = os.listdir(folder)
print(res)