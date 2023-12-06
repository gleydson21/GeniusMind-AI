// Função para obter as postagens
/*export function getPosts() {
    return fetch('https://api.example.com/posts')
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao obter as postagens.');
        }
        return response.json();
      })
      .then(data => {
        console.log(data); // Exibe as postagens no console
        return data;
      })
      .catch(error => {
        console.error(error);
        return null;
      });
  }
  
  // Função para criar uma nova postagem
  export function createPost(postData) {
    return fetch('https://api.example.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(postData)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao criar uma nova postagem.');
        }
        return response.json();
      })
      .then(data => {
        console.log(data); // Exibe a resposta da criação da postagem no console
        return data;
      })
      .catch(error => {
        console.error(error);
        return null;
      });
  }*/

// Pegando os dados do formulário
const form = document.querySelector('form');

form.addEventListener('submit', evento => {
  evento.preventDefault();

  const formData = new FormData(form)
  const dadosFormulario = Object.fromEntries(formData);

   fetch('http://127.0.0.1:5000/main.py', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(dadosFormulario)
  }).then(res => res.json())
    .then(data => {
      console.log(data);
    })
});

// // Função para obter os dados do arquivo .h5
// const form = document.querySelector('form');

// form.addEventListener('submit', evento => {
//   evento.preventDefault();

//   fetch('http://127.0.0.1:5000/main.py', {
//     method: 'POST',
//     // Não é necessário definir o cabeçalho Content-Type ou o corpo para solicitações GET
//   })
//     .then(res => res.json())
//     .then(data => {
//       console.log(data);
//       // Manipule os dados recebidos do servidor (dados.dados contém os dados do arquivo .h5)
//     })
//     .catch(error => {
//       console.error('Erro na solicitação:', error);
//     });
// });
