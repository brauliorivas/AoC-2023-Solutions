const part1 = (rawInput: string) => {
  const input = parseInput(rawInput)
  let lista: string[] = input.split("\n")
  let calibradores: number[] = lista.map((cali) => {
    const digits = cali.match(/\d/g)
    if (digits) {
      const digit1 = digits[0]
      const digit2 = digits[digits.length - 1]
      return parseInt(digit1) * 10 + parseInt(digit2)
    } else {
      return 0
    }
  })
  return calibradores.reduce((acc, val) => acc + val, 0)
}

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput)
  let lista: string[] = input.split("\n")
  let dig: number[] = lista.map((valores, index) => {
    let digitos: string[] = []
    let chars = valores.split("")
    chars.map((c, i) => {
      if (Number(c)) {
        digitos.push(c)
      }
      let numeros = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
      ]
      numeros.map((n, ni) => {
        if (valores.slice(i).startsWith(n)) {
          digitos.push(String(ni + 1))
        }
      })
    })

    return Number(digitos[0] + digitos[digitos.length - 1])
  })
  return dig.reduce((acc, val) => acc + val, 0)
}

