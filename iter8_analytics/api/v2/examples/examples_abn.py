"""
Examples used in A/B/n tests of iter8 analytics v2 APIs.
"""
# iter8 dependencies
from iter8_analytics.api.v2.examples.examples_metrics import \
    request_count, mean_latency, business_revenue

abn_mr_example = [request_count, mean_latency, business_revenue]

abn_er_example = {
    "spec": {
        "strategy": {
            "testingPattern": "A/B"
        },
        "versionInfo": {
            "baseline": {
                "name": "default",
                "variables": [{
                    "name": "container",
                    "value": "sklearn-iris-20"
                }]
            },
            "candidates": [
                {
                    "name": "canary1",
                    "variables": [{
                        "name": "container",
                        "value": "sklearn-iris-22"
                }]
                },
                {
                    "name": "canary2",
                    "variables": [{
                        "name": "container",
                        "value": "sklearn-iris-24"
                }]
                }
            ]
        },
        "criteria": {
            "objectives": [{
                "metric": "mean-latency",
                "upperLimit": 420.0
            }],
            "rewards": [{
                "metric": "business-revenue",
                "preferredDirection": "High"
            }]
        }
    },
    "status": {
        "startTime": "2020-04-03T12:55:50.568Z",
        "metrics": abn_mr_example
    },
}

abn_am_response = {
    "data": {
        "request-count": {
            "data": {
                "default": {
                    "value": '148.0405378277749'
                },
                "canary1": {
                    "value": '143.03538837774244'
                },
                "canary2": {
                    "value": '145.03478732974244'
                }
            }
        },
        "mean-latency": {
            "data": {
                "default": {
                    "value": '419.2027282381035'
                },
                "canary1": {
                    "value": '412.9510489510489'
                },
                "canary2": {
                    "value": '415.9573489510489'
                }
            }
        },
        "business-revenue": {
            "data": {
                "default": {
                    "value": '323.32'
                },
                "canary1": {
                    "value": '3343.2343'
                },
                "canary2": {
                    "value": '2326.2343'
                }
            }
        }
    },
    "message": "All ok"
}

abn_va_response = {
    "data": {
        "default": [
            True
        ],
        "canary1": [
            True
        ],
        "canary2": [
            True
        ]
    },
    "message": "All ok"
}

abn_wa_response = {
  "data": {
    "winnerFound": True,
    "winner": "canary2",
    "bestVersions": ["canary2"]
  },
  "message": "candidate satisfies all objectives"
}

abn_w_response = {
    "data": [{
        "name": "default",
        "value":93

    },{
        "name": "canary1",
        "value": 3

    },{
        "name": "canary2",
        "value": 4

    }],
    "message": "All ok"
}

abn_er_example_step1 = {
    "spec": abn_er_example["spec"],
    "status": {
        "startTime": "2020-04-03T12:55:50.568Z",
        "analysis": {
            "aggregatedMetrics": abn_am_response
        }
    }
}

abn_er_example_step2 = {
    "spec": abn_er_example["spec"],
    "status": {
        "startTime": "2020-04-03T12:55:50.568Z",
        "analysis": {
            "aggregatedMetrics": abn_am_response,
            "versionAssessments": abn_va_response
        }
    }
}

abn_er_example_step3 = {
    "spec": abn_er_example["spec"],
    "status": {
        "startTime": "2020-04-03T12:55:50.568Z",
        "analysis": {
            "aggregatedMetrics": abn_am_response,
            "versionAssessments": abn_va_response,
            "winnerAssessment": abn_wa_response
        }
    }
}
