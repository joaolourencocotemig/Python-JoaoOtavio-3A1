

const CORES_STATUS = {
    "Pendente": { badge: "warning", texto: "dark", borda: "border-warning" },
    "Em andamento": { badge: "primary", texto: "white", borda: "border-primary" },
    "Concluída": { badge: "success", texto: "white", borda: "border-success" },
};

let filtroAtual = "Todas";
let grafico = null;

function montarCardTarefa(tarefa) {
    const template = document.getElementById("templateCardTarefa");
    const clone = template.content.cloneNode(true);
    const cores = CORES_STATUS[tarefa.status] || CORES_STATUS["Pendente"];

    const cardEl = clone.querySelector(".tarefa-card");
    cardEl.classList.add(cores.borda);
    cardEl.classList.add("border-2");

    clone.querySelector(".tarefa-titulo").textContent = tarefa.titulo;
    clone.querySelector(".tarefa-descricao").textContent = tarefa.descricao || "Sem descrição.";

    const badge = clone.querySelector(".tarefa-badge");
    badge.textContent = tarefa.status;
    badge.classList.add(`bg-${cores.badge}`, `text-${cores.texto}`);

    clone.querySelector(".tarefa-editar").href = `/editar/${tarefa.id}`;

    const btnConcluir = clone.querySelector(".tarefa-concluir");
    if (tarefa.status === "Concluída") {
        btnConcluir.disabled = true;
        btnConcluir.classList.add("d-none");
    } else {
        btnConcluir.addEventListener("click", () => concluirTarefa(tarefa.id));
    }

    clone.querySelector(".tarefa-excluir").addEventListener("click", () => excluirTarefa(tarefa.id));

    return clone;
}

async function carregarTarefas(status = "Todas") {
    const lista = document.getElementById("listaTarefas");
    lista.innerHTML = '<div class="text-center text-muted py-4"><div class="spinner-border spinner-border-sm"></div> Carregando...</div>';

    try {
        const resposta = await fetch(`/api/tarefas?status=${encodeURIComponent(status)}`);
        if (!resposta.ok) throw new Error("Falha ao buscar tarefas.");
        const tarefas = await resposta.json();

        lista.innerHTML = "";

        if (tarefas.length === 0) {
            lista.innerHTML = `
                <div class="col-12 text-center text-muted py-5">
                    <i class="bi bi-inbox fs-1"></i>
                    <p class="mt-2">Nenhuma tarefa encontrada.</p>
                </div>`;
            return;
        }

        tarefas.forEach((tarefa) => {
            lista.appendChild(montarCardTarefa(tarefa));
        });
    } catch (erro) {
        lista.innerHTML = `<div class="col-12 alert alert-danger">Erro ao carregar tarefas: ${erro.message}</div>`;
    }
}

async function concluirTarefa(id) {
    try {
        const resposta = await fetch(`/api/tarefas/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: "Concluída" }),
        });
        if (!resposta.ok) throw new Error("Falha ao atualizar tarefa.");
        await atualizarTudo();
    } catch (erro) {
        alert(erro.message);
    }
}

async function excluirTarefa(id) {
    if (!confirm("Excluir esta tarefa?")) return;
    try {
        const resposta = await fetch(`/api/tarefas/${id}`, { method: "DELETE" });
        if (!resposta.ok) throw new Error("Falha ao excluir tarefa.");
        await atualizarTudo();
    } catch (erro) {
        alert(erro.message);
    }
}

async function carregarProgresso() {
    try {
        const resposta = await fetch("/api/progresso");
        if (!resposta.ok) throw new Error("Falha ao buscar progresso.");
        const dados = await resposta.json();

        document.getElementById("qtdPendente").textContent = dados["Pendente"] ?? 0;
        document.getElementById("qtdAndamento").textContent = dados["Em andamento"] ?? 0;
        document.getElementById("qtdConcluida").textContent = dados["Concluída"] ?? 0;

        const ctx = document.getElementById("graficoProgresso");
        const valores = [dados["Pendente"] ?? 0, dados["Em andamento"] ?? 0, dados["Concluída"] ?? 0];

        if (grafico) {
            grafico.data.datasets[0].data = valores;
            grafico.update();
            return;
        }

        grafico = new Chart(ctx, {
            type: "pie",
            data: {
                labels: ["Pendente", "Em andamento", "Concluída"],
                datasets: [{
                    data: valores,
                    backgroundColor: ["#ffc107", "#0d6efd", "#198754"],
                }],
            },
            options: {
                responsive: true,
                plugins: { legend: { position: "bottom" } },
            },
        });
    } catch (erro) {
        console.error(erro);
    }
}

async function atualizarTudo() {
    await Promise.all([carregarTarefas(filtroAtual), carregarProgresso()]);
}

document.addEventListener("DOMContentLoaded", () => {
    
    document.querySelectorAll(".filtro-opcao").forEach((opcao) => {
        opcao.addEventListener("click", (evento) => {
            evento.preventDefault();
            filtroAtual = opcao.dataset.status;
            document.getElementById("filtroLabel").textContent = filtroAtual;
            carregarTarefas(filtroAtual);
        });
    });

    atualizarTudo();
});
