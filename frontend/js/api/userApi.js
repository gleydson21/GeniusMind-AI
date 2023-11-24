// Função para obter os dados de um usuário
export function getUserData(userId) {
    return fetch(`https://api.example.com/users/${userId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao obter os dados do usuário.');
        }
        return response.json();
      })
      .then(data => {
        console.log(data); // Exibe os dados do usuário no console
        return data;
      })
      .catch(error => {
        console.error(error);
        return null;
      });
  }
  
  // Função para criar um novo usuário
  export function createNewUser(userData) {
    return fetch('https://api.example.com/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao criar um novo usuário.');
        }
        return response.json();
      })
      .then(data => {
        console.log(data); // Exibe a resposta da criação do usuário no console
        return data;
      })
      .catch(error => {
        console.error(error);
        return null;
      });
  }