find ./PDB_MIRROR/ -name "*.gz" > file_list.dat

a=`gawk '{print $1}' list/pdb_entry_type.txt`
for i in $a
do
  grep -q $i file_list.dat
  re="$?"
  if [ $re -eq 1 ]
  then
    echo $i >> pdb_no_file.dat
  fi
done

for i in `cat file_list.dat`
do
  grep -q ${i:19:4} list/pdb_entry_type.txt
  re="$?"
  if [ $re -eq 1 ]
  then
    echo ${i:19:4} >> pdb_no_list.dat
  fi
done
