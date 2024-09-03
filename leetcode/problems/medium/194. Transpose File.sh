#array=()
#while IFS= read -r line || [[ -n "$line" ]]; do
#  words=($(echo "$line" | sed ' '))
#  max=${#words[@]}
#  for (( i=1; i <= max+1; ++i ))
#  do
#    array[i]="${array[$i]} ${words[$i]}"
#  done
#done < file.txt
#
#max=${#array[@]}
#for (( i=1; i <= max-1; ++i ))
#do
#  echo "${array[i]}"
#done

awk '
{
    for (i = 1; i <= NF; i++)  {
        a[i] = a[i] ? a[i] " " $i : $i
    }
}
END {
    for (i = 1; i <= length(a); i++) {
        print a[i]
    }
}' file.txt