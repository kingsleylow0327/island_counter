# Argument Check
if [[ $# -eq 0 ]] ; then
    echo 'Missing Text Path. Try: sh ./run.sh <input>.txt"'
    exit -1
fi
# File Patch Check
if [ ! -f $1 ]; then
    echo $1 'is not a valid file'
    exit -1
fi
# File type check
if [[ "${1##*.}" != "txt" ]] ; then
    echo $1 'is not .txt file type'
    exit -1
fi
# Remove ./input.txt in project
if [ -f "./input.txt" ]; then
    rm ./input.txt
fi
# Copy argument file into projecy
cp $1 ./input.txt
# Delete Image is exsist
if [[ "$(docker images -q island_counter:0.1)" != "" ]]; then
  docker image rm island_counter:0.1
fi
# Docker build and run
docker image build -qt island_counter:0.1 -f "./dockerfile" .
docker run --rm island_counter:0.1