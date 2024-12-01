async function getPostos() {
    const listContainer = document.getElementById('postos-list');
    listContainer.innerHTML = '<p>Carregando...</p>'; 

    try {
        const response = await fetch('http://127.0.0.1:8000/postos-vacinacao/');
        const postos = await response.json();

        console.log(postos);

        if (!postos.length) {
            listContainer.innerHTML = '<p>Nenhum posto encontrado.</p>'; 
            return;
        }

        listContainer.innerHTML = ''; 

        postos.forEach(posto => {
            const postoElement = document.createElement('div');
            postoElement.classList.add('posto');
            postoElement.innerHTML = `
                <h3><i class="fas fa-clinic-medical"></i> ${posto.nome} - ${posto.cidade}</h3>
                <p><strong><i class="fas fa-map-marker-alt"></i> Endereço:</strong> <span>${posto.endereco}</span></p>
                <p><strong><i class="fas fa-clock"></i> Horário:</strong> <span>${posto.horario}</span></p>
                <p><strong><i class="fas fa-syringe"></i> Vacinas:</strong> <span>${Array.isArray(posto.vacinas) ? posto.vacinas.join(', ') : 'Não especificado'}</span></p>
            `;  
            listContainer.appendChild(postoElement);
        });
    } catch (error) {
        console.error('Erro ao carregar os postos:', error);
        listContainer.innerHTML = '<p>Erro ao carregar os postos. Tente novamente mais tarde.</p>';
    }
}

window.onload = getPostos;
