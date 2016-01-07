murmurhash3 = require('murmurhash3')

for line in io.stdin:lines() do
    io.stdout:write(string.format('%s\n', murmurhash3.hash32(line)))
end
