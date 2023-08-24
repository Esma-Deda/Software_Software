graph [
  directed 1
  name "Protein Interaction Graph"
  node [
    id 0
    label "PALB2"
  ]
  node [
    id 1
    label "ATM"
  ]
  node [
    id 2
    label "RAD51"
  ]
  node [
    id 3
    label "BRCA1"
  ]
  node [
    id 4
    label "BRCA2"
  ]
  edge [
    source 0
    target 1
    weight 0.945
  ]
  edge [
    source 0
    target 2
    weight 0.999
  ]
  edge [
    source 0
    target 3
    weight 0.999
  ]
  edge [
    source 0
    target 4
    weight 0.999
  ]
  edge [
    source 1
    target 4
    weight 0.995
  ]
  edge [
    source 1
    target 2
    weight 0.995
  ]
  edge [
    source 1
    target 3
    weight 0.999
  ]
  edge [
    source 3
    target 2
    weight 0.999
  ]
  edge [
    source 4
    target 2
    weight 0.999
  ]
  edge [
    source 4
    target 3
    weight 0.999
  ]
]
