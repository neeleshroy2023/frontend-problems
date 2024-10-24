var Stack = function() {
    this.storage = [];

    this.add = function(element) {
        this.storage.push(element)
        return this.storage.length
    }

    this.pop = function() {
        if (this.storage.length === 0) {
            return 'underflow'
        }
        this.storage.pop()
        return this.storage.length
    }

    this.peek = function() {
        if (this.storage.length === 0) return "No elements in stack"
        return this.storage[this.storage.length - 1]
    }

    this.isEmpty = function() {
        return this.storage.length === 0
    }

    this.printStack = function() {
        let str = ''
        for(let i=0; i<this.storage.length; i++) {
            str += this.storage[i] + ' '
        }
        return str
    }
}

var driver = new Stack()
console.log('stack')
let i = 10
while(i>0) {
    driver.add(Math.floor(Math.random() * 100))
    console.log('inserted elements ---> ', driver.peek())
    i--
}
console.log(driver.printStack())

i = 5
while(i>0) {
    driver.pop()
    console.log('removed elements ---> ', driver.peek())
    i--
}
console.log(driver.printStack())

console.log("driver is empty: ", driver.isEmpty())
