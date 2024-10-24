class Queue {
    constructor() {
        this.storage = []
    }

    size() {
        return this.storage.length
    }

    enqueue(element) {
        this.storage.unshift(element)
        return this.size()
    }

    dequeue() {
        this.storage.pop()
        return this.size()
    }

    peek() {
        if(this.size() === 0) return "No elements to peek :("
        return this.storage[this.size() - 1]
    }

    print() {
        let str = ''
        for(let i=0; i < this.size(); i++) {
            str += this.storage[i] + ' '
        }
        return str
    }

    isEmpty() {
        return this.size() === 0
    }
}

var driver = new Queue()
console.log('queue')
let i = 10
while(i>0) {
    driver.enqueue(Math.floor(Math.random() * 100))
    i--
}
console.log("elements inserted ---")
console.log(driver.print())

i = 5
while(i>0) {
    console.log('removing elements --- ', driver.peek())
    driver.dequeue()
    i--
}
console.log(driver.print())

console.log("driver is empty: ", driver.isEmpty())