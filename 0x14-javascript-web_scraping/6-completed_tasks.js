#!/usr/bin/node
/* Numero de tareas completadas por id del usuario
- 1er argumento - url solicitada
- solo printear usuarios con tareas completadas
- usando axios
*/
const axios = require('axios').default;

const url = process.argv[2];

axios.get(url)
  .then((res) => {
    const tareas = res.data;
    const dic = {};
    for (const task of tareas) {
      if (task.completed === true) {
        if (dic[task.userId] === undefined) { dic[task.userId] = 1; } else { dic[task.userId]++; }
      }
    }
    console.log(dic);
  });
