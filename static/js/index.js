let tempoAgora = '';

tempoAgora += 
    `
    <p>descricao</p>
    <div>
        <div><p>icon</p></div>
        <div>
            <p>temp</p>
            <p>descricao temp</p>
        </div>
        <div>
            <p>direcao vento</p>
            <p>sentido<br>velocidade</p>
        </div>
    </div>`;

document.getElementById('wheaterNow').innerHTML = tempoAgora;