import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar a largura total e esconder o menu lateral do Streamlit
st.set_page_config(
    page_title="Calculadora de Devolução",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo para remover margens padrão do Streamlit e fazer o site ocupar tudo
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# O código HTML completo que organizamos no Canvas
# (Aqui inserimos o código exatamente como está no seu ficheiro .html)
html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Devolução - Financeiro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f3f4f6; }
        .sidebar-gradient { background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); }
        .header-blue { background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); }
        .section-header { border-left: 4px solid #2563eb; padding-left: 1rem; }
        .card-input { background-color: #ffffff; border: 1px solid #e5e7eb; }
        .card-result { background-color: #ffffff; border: 1px solid #e2e8f0; transition: all 0.2s; }
        .card-result:hover { border-color: #3b82f6; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .card-devolucao-container { background: #ffffff; border: 2px solid #22c55e; border-radius: 1.5rem; }
        .active-nav { background-color: #2563eb !important; color: white !important; }
        .copy-toast { position: fixed; bottom: 20px; right: 20px; background: #1e293b; color: #ffffff; padding: 12px 24px; border-radius: 8px; display: none; z-index: 9999; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        input:focus { box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2); }
        .btn-copy { cursor: pointer; transition: transform 0.1s; }
        .btn-copy:active { transform: scale(0.98); }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
    </style>
</head>
<body class="flex min-h-screen">
    <div id="toast" class="copy-toast">Valor copiado!</div>
    <aside class="w-72 sidebar-gradient text-white flex flex-col sticky top-0 h-screen shadow-2xl">
        <div class="p-8 text-center border-b border-slate-700">
            <h1 class="text-xl font-extrabold tracking-tight italic">💰 CALCULADORA</h1>
            <p class="text-blue-400 text-[10px] font-bold uppercase mt-1 tracking-widest text-center">Devolução & Descontos</p>
        </div>
        <nav class="flex-1 p-4 space-y-2">
            <button onclick="showPage('nfd', this)" id="btn-nfd" class="nav-btn active-nav w-full flex items-center px-4 py-3 text-sm font-semibold rounded-lg transition-all hover:bg-slate-800">
                <span class="mr-3 text-lg">📋</span> Devolução NFD
            </button>
            <button onclick="showPage('sb', this)" id="btn-sb" class="nav-btn w-full flex items-center px-4 py-3 text-sm font-semibold rounded-lg transition-all text-slate-300 hover:bg-slate-800">
                <span class="mr-3 text-lg">🏭</span> Fornecedor SB
            </button>
            <button onclick="showPage('custo', this)" id="btn-custo" class="nav-btn w-full flex items-center px-4 py-3 text-sm font-semibold rounded-lg transition-all text-slate-300 hover:bg-slate-800">
                <span class="mr-3 text-lg">⚖️</span> Custo de Aquisição
            </button>
            <button onclick="showPage('conversor', this)" id="btn-conversor" class="nav-btn w-full flex items-center px-4 py-3 text-sm font-semibold rounded-lg transition-all text-slate-300 hover:bg-slate-800">
                <span class="mr-3 text-lg">📏</span> Conversor de Unidade
            </button>
        </nav>
        <div class="p-6 border-t border-slate-700 text-center text-slate-500">
            <p class="text-[10px] font-medium uppercase tracking-widest">v2.6 - COMPLETA</p>
        </div>
    </aside>

    <main class="flex-1 p-8 lg:p-12 overflow-y-auto bg-slate-50">
        <!-- ABA: NFD -->
        <div id="page-nfd" class="page-content animate-fade-in">
            <header class="header-blue p-8 rounded-2xl text-white mb-10 shadow-lg">
                <h2 class="text-4xl font-extrabold">Devolução NFD</h2>
                <p class="text-blue-100 mt-2 font-medium">Cálculo de abatimento e descontos para Nota Fiscal de Devolução.</p>
            </header>
            <div class="space-y-12">
                <div class="card-input p-8 rounded-2xl shadow-sm border-t-4 border-t-blue-500">
                    <div class="section-header mb-6"><h3 class="font-bold text-slate-700 uppercase tracking-wider text-sm">Dados da Operação</h3></div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div><label class="block text-[10px] font-bold text-slate-400 uppercase mb-1">Valor Total do Produto</label><input type="text" id="n-total-bruto" value="0,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-bold text-slate-700 outline-none focus:border-blue-500"></div>
                        <div><label class="block text-[10px] font-bold text-slate-400 uppercase mb-1">Valor Total da Nota</label><input type="text" id="n-total-nota" value="0,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-bold text-slate-700 outline-none focus:border-blue-500"></div>
                        <div><label class="block text-[10px] font-bold text-slate-400 uppercase mb-1">Quantidade</label><input type="number" id="n-qtd" value="1" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-bold text-slate-700 outline-none focus:border-blue-500"></div>
                        <div><label class="block text-[10px] font-bold text-slate-400 uppercase mb-1">Valor Unitário (4 casas)</label><input type="text" id="n-unit-bruto" value="0,0000" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-bold text-slate-700 outline-none focus:border-blue-500"></div>
                    </div>
                    <button onclick="calcNFD()" class="mt-8 w-full bg-blue-600 text-white font-extrabold py-4 rounded-xl shadow-lg hover:bg-blue-700 transition-all active:scale-95 uppercase tracking-widest text-sm">Calcular Desconto</button>
                </div>
                <div id="n-results" class="hidden">
                    <div class="section-header mb-6"><h3 class="font-bold text-slate-700 uppercase tracking-wider text-sm">Resultados do Cálculo</h3></div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="card-result p-6 rounded-2xl shadow-sm"><p class="text-[10px] font-bold text-slate-400 uppercase flex items-center gap-1">📊 Desconto (%)</p><p id="res-n-perc" class="text-4xl font-black text-slate-800 mt-1">0,00%</p></div>
                        <div class="card-result p-6 rounded-2xl shadow-sm"><p class="text-[10px] font-bold text-blue-500 uppercase flex items-center gap-1">🏷️ Unitário c/ Desconto</p><p id="res-n-unit-pago" class="text-4xl font-black text-blue-600 mt-1">R$ 0,0000</p></div>
                        <div class="card-result p-6 rounded-2xl shadow-sm"><p class="text-[10px] font-bold text-orange-500 uppercase flex items-center gap-1">🎯 Desconto por Peça</p><p id="res-n-unit-desc" class="text-4xl font-black text-orange-600 mt-1">R$ 0,0000</p></div>
                        <div class="card-result p-6 rounded-2xl shadow-sm"><p class="text-[10px] font-bold text-slate-400 uppercase flex items-center gap-1">💰 Total sem Desconto</p><p id="res-n-total-original" class="text-4xl font-black text-slate-800 mt-1">R$ 0,00</p></div>
                        <div class="card-result p-6 rounded-2xl shadow-sm"><p class="text-[10px] font-bold text-green-600 uppercase flex items-center gap-1">💵 Total c/ Desconto</p><p id="res-n-total-desc" class="text-4xl font-black text-slate-800 mt-1">R$ 0,00</p></div>
                        <div class="card-result p-6 rounded-2xl shadow-sm border-2 border-slate-100"><p class="text-[10px] font-extrabold text-green-600 lowercase mb-0.5 leading-none">desconto unitário</p><p class="text-[10px] font-bold text-slate-400 uppercase flex items-center gap-1">💸 Desconto Total</p><p id="res-n-total-diferenca" class="text-4xl font-black text-slate-700 mt-1">R$ 0,00</p></div>
                    </div>
                    <div class="mt-12">
                        <div class="section-header mb-6"><h3 class="font-bold text-slate-700 uppercase tracking-wider text-sm">Cálculo para Devolução (NFD)</h3></div>
                        <div class="card-devolucao-container p-10 shadow-xl flex flex-col lg:flex-row items-center justify-between gap-12 border-green-500">
                            <div class="w-full lg:w-80"><label class="block text-[11px] font-black text-green-700 uppercase mb-3 text-center lg:text-left">Quantidade para Devolução</label><input type="number" id="n-qtd-dev" value="1" min="1" oninput="updateDevNFD()" class="w-full p-5 bg-slate-50 border-2 border-slate-100 rounded-2xl text-5xl font-black text-slate-800 text-center outline-none focus:border-green-400 focus:bg-white transition-all"></div>
                            <div class="flex-1 text-center btn-copy" onclick="copy('res-n-total-dev')">
                                <p class="text-sm font-bold text-green-600 uppercase flex items-center justify-center gap-3">💰 Valor Total de Desconto <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" /></svg></p>
                                <h2 id="res-n-total-dev" class="text-8xl font-black text-green-700 mt-2 leading-none">R$ 0,00</h2>
                                <p class="text-[11px] text-green-600 font-bold mt-6 bg-green-50 inline-block px-6 py-2 rounded-full border border-green-200 italic tracking-wide">Use este valor no campo 'desconto' da NFD</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ABA: SB -->
        <div id="page-sb" class="page-content hidden animate-fade-in">
             <header class="bg-slate-800 p-8 rounded-2xl text-white mb-10 shadow-lg border-b-4 border-blue-500"><h2 class="text-3xl font-extrabold italic">Cálculo Fornecedor SB</h2><p class="text-slate-300 mt-2 font-medium">Focado no Valor Unitário Pago (Preço Final).</p></header>
             <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
                <div class="xl:col-span-1 space-y-6">
                    <div class="card-input p-6 rounded-xl shadow-sm space-y-4">
                        <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Quantidade de Peças</label><input type="text" id="s-qtd" value="10,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold outline-none"></div>
                        <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Valor Unitário Bruto</label><input type="text" id="s-unit-bruto" value="1,0000" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold outline-none"></div>
                        <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Valor Total Líquido (Pago)</label><input type="text" id="s-total-pago" value="2,50" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold outline-none"></div>
                        <button onclick="calcSB()" class="w-full bg-blue-600 text-white font-bold py-4 rounded-lg shadow-md uppercase text-sm tracking-widest">Calcular Desconto</button>
                    </div>
                </div>
                <div class="xl:col-span-2 space-y-8">
                    <div id="s-results" class="hidden">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="metric-container p-6 rounded-xl shadow-sm bg-white border-blue-200"><p class="text-blue-600 text-sm font-extrabold uppercase leading-tight">🏷️ valor unitário do desconto</p><p id="res-s-unit-pago" class="text-4xl font-black text-blue-700 mt-1">R$ 0,0000</p><p class="text-slate-400 text-[10px] font-bold mt-6 uppercase leading-tight">💰 Valor Total Bruto</p><p id="res-s-total-bruto" class="text-2xl font-bold text-slate-800 mt-1">R$ 10,00</p></div>
                            <div class="metric-container p-6 rounded-xl shadow-sm text-right bg-orange-50 border-orange-200"><p class="text-orange-600 text-sm font-extrabold uppercase leading-tight">📈 Desconto (%)</p><p id="res-s-perc" class="text-4xl font-black text-orange-700 mt-1">0,00%</p><p class="text-orange-500 text-[10px] font-bold mt-6 uppercase leading-tight">💵 Valor com desconto (Abatido)</p><p id="res-s-unit-desc" class="text-2xl font-bold text-orange-700 mt-1">R$ 0,0000</p></div>
                        </div>
                        <div class="mt-8">
                             <div class="card-devolucao-container p-8 shadow-lg flex flex-col md:flex-row items-center justify-between gap-8 border-blue-500">
                                <div class="w-full md:w-48 text-center md:text-left"><label class="block text-xs font-extrabold text-blue-700 uppercase mb-2">Peças Devolvidas</label><input type="number" id="s-qtd-dev" value="0" oninput="updateDevSB()" class="w-full p-4 border-2 border-blue-100 rounded-xl text-3xl font-black text-slate-800 text-center outline-none"></div>
                                <div class="flex-1 text-center btn-copy" onclick="copy('res-s-total-dev')">
                                    <p class="text-xs font-bold text-green-600 uppercase flex items-center justify-center gap-2">Valor Total para Devolução <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" /></svg></p>
                                    <h2 id="res-s-total-dev" class="text-5xl font-black text-green-700 mt-1 italic">R$ 0,00</h2>
                                    <p class="text-[10px] text-green-500 font-bold mt-2 italic text-center leading-none">(Preço Pago Unitário × Qtd)</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
             </div>
        </div>

        <!-- ABA: CUSTO -->
        <div id="page-custo" class="page-content hidden animate-fade-in">
             <header class="header-blue p-8 rounded-2xl text-white mb-10 shadow-lg"><h2 class="text-3xl font-extrabold">Custo de Aquisição</h2></header>
             <div class="card-input p-10 rounded-2xl shadow-sm">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
                    <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Valor da Nota</label><input type="text" id="c-nota" value="0,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold"></div>
                    <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Frete</label><input type="text" id="c-frete" value="0,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold"></div>
                    <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">IPI</label><input type="text" id="c-ipi" value="0,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold"></div>
                </div>
                <button onclick="calcCusto()" class="w-full bg-blue-600 text-white font-bold py-4 rounded-lg shadow-lg hover:bg-blue-700">Calcular Custo</button>
                <div id="c-results" class="hidden w-full mt-8 text-center card-devolucao-container p-10 border-green-600">
                    <h2 id="res-c-total" class="text-5xl font-black text-green-700 mt-1">R$ 0,00</h2>
                </div>
             </div>
        </div>

        <!-- ABA: CONVERSOR -->
        <div id="page-conversor" class="page-content hidden animate-fade-in">
             <header class="header-blue p-8 rounded-2xl text-white mb-10 shadow-lg"><h2 class="text-3xl font-extrabold">Conversor Caixa/Peça</h2></header>
             <div class="max-w-xl mx-auto card-input p-8 rounded-2xl shadow-sm space-y-6">
                <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Quantidade por Caixa</label><input type="text" id="v-qtd-caixa" value="1,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold"></div>
                <div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Valor da Caixa</label><input type="text" id="v-total-caixa" value="0,00" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-lg font-semibold"></div>
                <button onclick="calcConv()" class="w-full bg-blue-600 text-white font-bold py-4 rounded-lg shadow-md hover:bg-blue-700 transition-all uppercase text-sm tracking-widest">Converter</button>
                <div id="v-results" class="hidden text-center card-devolucao-container p-12 border-green-600 btn-copy" onclick="copy('res-v-unit')">
                    <h2 id="res-v-unit" class="text-6xl font-black text-green-700 mt-1">R$ 0,0000</h2>
                </div>
             </div>
        </div>
    </main>

    <script>
        let state = { nfdUnitDesc: 0, sbUnitPaid: 0, convUnit: 0 };
        const fmt = (v, c = 2) => v.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: c, maximumFractionDigits: c });
        const parse = (s) => { if (!s) return 0; const val = parseFloat(s.toString().replace(/R\$\s?/, '').trim().replace(/\./g, '').replace(',', '.')); return isNaN(val) ? 0 : val; };
        function showPage(pId, btn) {
            document.querySelectorAll('.page-content').forEach(p => p.classList.add('hidden'));
            document.getElementById('page-' + pId).classList.remove('hidden');
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active-nav', 'text-white'));
            btn.classList.add('active-nav', 'text-white');
        }
        function copy(id) {
            const text = document.getElementById(id).innerText;
            const val = text.replace(/R\$\s?/, '').trim();
            const el = document.createElement('input'); el.value = val; document.body.appendChild(el); el.select();
            document.execCommand('copy'); document.body.removeChild(el);
            const t = document.getElementById('toast'); t.style.display = 'block';
            setTimeout(() => t.style.display = 'none', 2000);
        }
        function calcNFD() {
            const tBruto = parse(document.getElementById('n-total-bruto').value);
            const tNota = parse(document.getElementById('n-total-nota').value);
            const unitB = parse(document.getElementById('n-unit-bruto').value);
            const qtd = parse(document.getElementById('n-qtd').value) || 1;
            if (tBruto === 0) return;
            const pDesc = (1 - (tNota / tBruto)) * 100;
            const unitPaid = unitB * (1 - (pDesc / 100));
            const uAbate = unitB - unitPaid;
            state.nfdUnitDesc = uAbate;
            document.getElementById('res-n-perc').innerText = `${pDesc.toFixed(2).replace('.', ',')}%`;
            document.getElementById('res-n-unit-pago').innerText = fmt(unitPaid, 4);
            document.getElementById('res-n-unit-desc').innerText = fmt(uAbate, 4);
            document.getElementById('res-n-total-original').innerText = fmt(qtd * unitB);
            document.getElementById('res-n-total-desc').innerText = fmt(tNota);
            document.getElementById('res-n-total-diferenca').innerText = fmt((qtd * unitB) - tNota);
            document.getElementById('n-results').classList.remove('hidden');
            updateDevNFD();
        }
        function updateDevNFD() {
            const q = parse(document.getElementById('n-qtd-dev').value) || 0;
            document.getElementById('res-n-total-dev').innerText = fmt(q * state.nfdUnitDesc);
        }
        function calcSB() {
            const q = parse(document.getElementById('s-qtd').value) || 1;
            const uB = parse(document.getElementById('s-unit-bruto').value);
            const tL = parse(document.getElementById('s-total-pago').value);
            const tBruto = q * uB;
            const uPaid = tL / q;
            const uAbate = (tBruto - tL) / q;
            const p = ((tBruto - tL) / tBruto) * 100;
            state.sbUnitPaid = uPaid;
            document.getElementById('res-s-unit-pago').innerText = fmt(uPaid, 4);
            document.getElementById('res-s-total-bruto').innerText = fmt(tBruto);
            document.getElementById('res-s-perc').innerText = `${p.toFixed(2).replace('.', ',')}%`;
            document.getElementById('res-s-unit-desc').innerText = fmt(uAbate, 4);
            document.getElementById('s-results').classList.remove('hidden');
            updateDevSB();
        }
        function updateDevSB() {
            const q = parse(document.getElementById('s-qtd-dev').value) || 0;
            document.getElementById('res-s-total-dev').innerText = fmt(q * state.sbUnitPaid);
        }
        function calcCusto() {
            const n = parse(document.getElementById('c-nota').value);
            const f = parse(document.getElementById('c-frete').value);
            const i = parse(document.getElementById('c-ipi').value);
            document.getElementById('res-c-total').innerText = fmt(n + f + i);
            document.getElementById('c-results').classList.remove('hidden');
        }
        function calcConv() {
            const q = parse(document.getElementById('v-qtd-caixa').value) || 1;
            const t = parse(document.getElementById('v-total-caixa').value);
            state.convUnit = t / q;
            document.getElementById('res-v-unit').innerText = fmt(state.convUnit, 4);
            document.getElementById('v-results').classList.remove('hidden');
        }
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('blur', function() {
                const val = parse(this.value);
                const isFour = (this.id.includes('unit') || this.id.includes('bruto'));
                if(this.type !== 'number') this.value = val.toLocaleString('pt-BR', { minimumFractionDigits: isFour ? 4 : 2, maximumFractionDigits: isFour ? 4 : 2 });
            });
        });
    </script>
</body>
</html>
"""

# Renderizar no Streamlit com altura suficiente para não haver scroll duplo
components.html(html_code, height=1400, scrolling=True)
