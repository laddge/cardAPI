# cardAPI
New Blog Card API
## Usage
1. Import JS

```
<script type="text/javascript" src="https://cardapi.laddge.net/files/cardapi.min.js"></script>
```

2. Create an instance

```JavaScript
let cardAPIInstance = new CardAPI(className, template, override);
cardAPIInstance.load();
```

```className``` : class name of a-tag  
```template``` : HTML template  
```override``` : (boolean) whether to overwrite a-tag (default: true)  

### Template
You can use data from API in the template.
* ```{{ href }}```
* ```{{ title }} ```
* ```{{ description }}```
* ```{{ site_name }}```
* ```{{ image }}```

## Example
Please see [my CodePen](https://codepen.io/laddge/pen/yLMvrBZ).

## Warning
Specifications may change suddenly. If that doesn't work, please check here.

## Licence
This source is under the MIT-License.

See also [LICENSE](LICENSE).

## Author
Laddge
