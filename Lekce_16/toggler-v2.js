class Toggler {
    constructor(button) {
        this.button = button;
        this.data = JSON.parse(button.dataset.toggle);
        button.addEventListener('click', e => this.toggle());
    }

    toggle() {
        for (let key in this.data) {
            let parent = key[0] === ':' ? this.button : document;
            let element = parent.querySelector(key);
            let attrs = this.data[key];
            this.toggleItem(element, attrs);
        }
    }

    toggleItem(element, attrs) {
        for (let attr in attrs) {
            let value = attrs[attr];
            attr === 'class' ?
            element.classList.toggle(value) :
            toggleAttr(element, attr, value);
        }
    }
}

function toggleAttr(element, attr, value) {
    let key = 'toggle' + attr;
    let currentValue = element.getAttribute(attr);
    let originalValue = element.dataset[key] || currentValue;

    if (!element.dataset[key]) {
        element.dataset[key] = originalValue;
    }

    element.setAttribute(attr, currentValue === value ? originalValue : value);
}

let buttons = document.querySelectorAll('[data-toggle]');
buttons.forEach(button => {
    new Toggler(button);
});