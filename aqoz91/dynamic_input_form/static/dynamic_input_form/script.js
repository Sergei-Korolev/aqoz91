var Counter = function() {
        var i = 1;

        return function() {
            return i++;
        };
    };

var counter = Counter();


function add_element() {
    var step = counter();
    var element = document.getElementById('bttn_sub');
    var p = document.createElement('p');
    var label = document.createElement('label');
    var input = document.createElement('input');

    p.id = 'p_id_name' + step;

    label.innerHTML = 'Name' + step + ':';
    label.htmlFor = 'id_name' + step;

    input.type = 'text';
    input.name = 'name' + step;
    input.required = true;
    input.id = 'id_name' + step;

    element.before(p);
    p.appendChild(label);
    p.appendChild(input);

};
