var pie = new d3pie("pieChart", {
    "header": {
        "title": {
            "text": "CAssistant",
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
        "canvasHeight": 400,
        "canvasWidth": 590,
        "pieInnerRadius": "30%",
        "pieOuterRadius": "90%"
    },
    "data": {
        "content": [
            {
                "label": "Агрессия",
                "value": 8,
                "color": "#0066cc"
            },
            {
                "label": "Интеллект",
                "value": 5,
                "color": "#003366"
            },
            {
                "label": "Хуй",
                "value": 2,
                "color": "#336600"
            },
            {
                "label": "Пизда",
                "value": 3,
                "color": "#669966"
            },
            {
                "label": "Доброжелательность",
                "value": 2,
                "color": "#990000"
            },
            {
                "label": "ЛолКекЧебурек",
                "value": 1,
                "color": "#cc6600"
            }
        ]
    },
    "labels": {
        "outer": {
            "pieDistance": 16
        },
        "mainLabel": {
            "font": "verdana"
        },
        "percentage": {
            "color": "#e1e1e1",
            "font": "verdana",
            "decimalPlaces": 0
        },
        "value": {
            "color": "#e1e1e1",
            "font": "verdana"
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
});

var pie = new d3pie("secondPie", {
    "header": {
        "title": {
            "text": "CAssistant",
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
        "canvasHeight": 400,
        "canvasWidth": 590,
        "pieInnerRadius": "30%",
        "pieOuterRadius": "90%"
    },
    "data": {
        "content": [
            {
                "label": "Агрессия",
                "value": 8,
                "color": "#0066cc"
            },
            {
                "label": "Интеллект",
                "value": 5,
                "color": "#003366"
            },
            {
                "label": "Хуй",
                "value": 2,
                "color": "#336600"
            },
            {
                "label": "Пизда",
                "value": 3,
                "color": "#669966"
            },
            {
                "label": "Доброжелательность",
                "value": 2,
                "color": "#990000"
            },
            {
                "label": "ЛолКекЧебурек",
                "value": 1,
                "color": "#cc6600"
            }
        ]
    },
    "labels": {
        "outer": {
            "pieDistance": 16
        },
        "mainLabel": {
            "font": "verdana"
        },
        "percentage": {
            "color": "#e1e1e1",
            "font": "verdana",
            "decimalPlaces": 0
        },
        "value": {
            "color": "#e1e1e1",
            "font": "verdana"
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
});