let buttons = document.querySelectorAll('[data-toggle]');
buttons.forEach(button => {
    let toggle = JSON.parse(button.dataset.toggle);
    for (let key in toggle) {
        button.addEventListener('click', e => {
            let parent = key[0] === ':' ? button : document;
            let element = parent.querySelector(key);
            let attrs = toggle[key];
            for (let attr in attrs) {
                let value = attrs[attr];
                if (attr === 'class') {
                    element.classList.toggle(value);
                } else {
                    let actValue = element.getAttribute(attr);
                    let oldAttr = 'old-' + attr;
                    if (!element.hasAttribute(oldAttr)) {
                        element.setAttribute(oldAttr, actValue);
                    }
                    if (actValue === value) {
                        element.setAttribute(attr, element.getAttribute(oldAttr));
                    } else {
                        element.setAttribute(attr, value);
                    }
                }
            }
        });
    }
});