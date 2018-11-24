var firstPieData = [
    {
        "label": "Эмпатийность",
        "value": 8,
        "color": "#0066cc"
    },
    {
        "label": "Нейротизм",
        "value": 3,
        "color": "#669966"
    },
    {
        "label": "Интеллект",
        "value": 8,
        "color": "#336600"
    }
];

var secondPieData = [
    {
        "label": "Экстраверсия",
        "value": 5,
        "color": "#ff9900"
    },
    {
        "label": "Интроверсия",
        "value": 5,
        "color": "#5058ed"
    }
];

var thirdPieData = [
    {
        "label": "Агрессия",
        "value": 4,
        "color": "#67f200"
    },
    {
        "label": "Манипуляция",
        "value": 4,
        "color": "#01503d"
    },
    {
        "label": "Эгоцентризм",
        "value": 4,
        "color": "#d0ff00"
    }
];

function generatePie(data){
    return {
    "header": {
        "title": {
            "text": "",
            "color": "#181515",
            "fontSize": 22,
            "font": "open sans"
        },
        "subtitle": {
            "color": "#999999",
            "fontSize": 10,
            "font": "open sans"
        },
        "titleSubtitlePadding": 1
    },
    "footer": {
        "color": "#999999",
        "fontSize": 11,
        "font": "open sans",
        "location": "bottom-center"
    },
    "size": {
        "canvasHeight": 200,
        "canvasWidth": 390,
        "pieInnerRadius": "30%",
        "pieOuterRadius": "90%"
    },
    "data": {
        "content": data
    },
    "labels": {
        "outer": {
            "pieDistance": 16
        },
        "mainLabel": {
            "font": "verdana",
            "fontSize": 16
        },
        "percentage": {
            "color": "#e1e1e1",
            "font": "verdana",
            "decimalPlaces": 0
        },
        "value": {
            "color": "#e1e1e1",
            "font": "verdana",
            "fontSize": 16
        },
        "lines": {
            "enabled": true,
            "color": "#cccccc"
        },
        "truncation": {
            "enabled": true
        }
    },
    "effects": {
        "pullOutSegmentOnClick": {
            "effect": "linear",
            "speed": 400,
            "size": 8
        }
    },
    "misc": {
        "gradient": {
            "enabled": true,
            "percentage": 66,
            "color": ""
        }
    }
};
}

var firstPie = new d3pie("empathyPie", generatePie(firstPieData));
var secondPie = new d3pie("extraversionPie", generatePie(secondPieData));
var thirdPie = new d3pie("aggroEgoManPie", generatePie(thirdPieData));

function getUpdates(){
    var url = "https://ghw18.herokuapp.com/data";
    $.post(url, 1, (data) => { // TODO: change 1 to null
        console.log("trying to get data...");
        console.log(data);
        applyUpdates(data);
    }, "text");
}

function applyUpdates(data){
    if (data != "null"){
        data = JSON.parse(data);
        firstPieData[0].value  = data[2];
        firstPieData[1].value  = data[1];
        firstPieData[2].value  = data[3];
        secondPieData[0].value = data[0];
        secondPieData[1].value = 100 - secondPieData[0].value;
        thirdPieData[0].value  = data[4];
        thirdPieData[1].value  = data[5];
        thirdPieData[2].value  = data[6];
        firstPie.updateProp("data.content", firstPieData);
        secondPie.updateProp("data.content", secondPieData);
        thirdPie.updateProp("data.content", thirdPieData);
        $(".loading").addClass("invisible");
    }
}
setTimeout(() => {
    getUpdates();
}, 1500);
setInterval(() => {
    getUpdates();
}, 10000);



