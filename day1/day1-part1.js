const fs = require('fs')
const readline = require('readline')

const countIncreases = async (lines) => {
    let increases = 0
    let lastNumber = null
    for await (const line of lines) {
        const nextNumber = Number(line)
        increases += (lastNumber && lastNumber < nextNumber) ? 1 : 0
        lastNumber = nextNumber
    }
    return increases
}

const lines = readline.createInterface({
    input: fs.createReadStream('input')
})

countIncreases(lines)
    .then(r => console.log(`Number of increases: ${r}`))
    .catch(b => console.error(b))