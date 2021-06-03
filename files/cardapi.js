function CardAPI(className, template, override = true) {
    this.load = function () {
        for (const elem of document.getElementsByClassName(className)) {
            if (elem.href) {
                const api = 'https://cardapi.laddge.tk/?url=' + encodeURI(elem.href);
                fetch(api)
                    .then(data => {
                        return data.json();
                    })
                    .then(json => {
                        if (json != {}) {
                            const rendered = template
                                .replace(/{{ title }}/g, json.title)
                                .replace(/{{ description }}/g, json.description)
                                .replace(/{{ site_name }}/g, json.site_name)
                                .replace(/{{ image }}/g, json.image);
                            if (override) {
                                elem.outerHTML = rendered;
                            } else {
                                elem.innerHTML = rendered;
                            }
                        }
                    });
            }
        }
    };
}
