function CardAPI(className, template, override = true) {
    'use strict';
    this.load = function() {
        for (const elem of document.getElementsByClassName(className)) {
            if (elem.href) {
                const api = 'https://cardapi.laddge.tk/?url=' + encodeURI(elem.href);
                fetch(api)
                    .then(data => {
                        return data.json();
                    })
                    .then(json => {
                        if (data != {}) {
                            const rendered = template
                                .replace(/{{ title }}/g, data.title)
                                .replace(/{{ description }}/g, data.description)
                                .replace(/{{ site_name }}/g, data.site_name)
                                .replace(/{{ image }}/g, data.image);
                            if (override) {
                                elem.outerHTML = rendered;
                            } else {
                                elem.innerHTML = rendered;
                            }
                        }
                    });
            }
        }
    }
}
