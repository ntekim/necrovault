cd necro-engine
go build -o ../necro-mcp ./cmd/mcp/main.go
cd ..

# Create a mock 90s binary (Flash SWF signature)
printf "FWS\x08\x00\x00\x00" > sample_legacy.swf

# Run the Python Brain
python3 python/agent/necro_brain.py sample_legacy.swf

# Create a file with the Flash CWS (compressed SWF) header
printf "CWS\x09\x10\x00\x00\x00" > test_legacy.swf

./necro-cli -file test_legacy.swf -out resurrected.html