/*!
  * cardAPI (https://github.com/laddge/cardAPI)
  * Copyright 2021 Laddge
  * Licensed under MIT (https://github.com/laddge/cardAPI/blob/master/LICENSE)
  */
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
                        if (Object.keys(json).length) {
                            const rendered = template
                                .replace(/{{ href }}/g, elem.href)
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
