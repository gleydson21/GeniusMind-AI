// Coleta os dados do formulário
const formData = {
  idade: document.getElementById('idade').value,
  sexo: document.getElementById('sexo').value,
  escolaridade: document.getElementById('escolaridade').value,
  bolsa: document.getElementById('bolsa').value,
  trabalho_adicional: document.getElementById('trabalho-adicional').value,
  horas_estudadas: document.getElementById('horas-estudadas').value,
  impactos_atividades: document.getElementById('impactos-atividades').value,
  frequencia_aulas: document.getElementById('frequencia-aulas').value,
  discussao: document.getElementById('discussao').value,
  media: document.getElementById('media').value,
  Id_Curso: document.getElementById('Id-Curso').value,
};

// Envia os dados para o backend usando a API fetch
try {
  const response = await fetch('http://127.0.0.1:500/enviar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', // Define o tipo de mídia como JSON
    },
    body: JSON.stringify(formData), // Converte os dados para JSON
  });

  if (response.ok) {
    const result = await response.json();
    console.log('Resposta do servidor:', result);
    // Faça algo com a resposta do servidor
  } else {
    console.error('Erro na solicitação:', response.statusText);
    // Faça algo em caso de erro na solicitação
  }
} catch (error) {
  console.error('Erro na requisição:', error);
  // Faça algo em caso de exceção
}
