import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Função de produção
def production_function(k, alpha):
    return k ** alpha

# Funções auxiliares para o modelo
def update_curves(k_vals, s, n, d, alpha):
    y_vals = production_function(k_vals, alpha)
    sy_vals = s * y_vals
    dep_vals = (n + d) * k_vals
    c_vals = y_vals - sy_vals
    return y_vals, sy_vals, dep_vals, c_vals

def find_steady_state(s, n, d, alpha):
    k_star = (s / (n + d)) ** (1 / (1 - alpha))
    y_star = production_function(k_star, alpha)
    c_star = y_star - s * y_star
    w_star = (1 - alpha) * k_star ** alpha
    r_star = alpha * k_star ** (alpha - 1)
    return k_star, y_star, c_star, w_star, r_star

# Interface do Streamlit
st.title("Modelo de Solow Simples ")
st.markdown("Ajuste os parâmetros abaixo para visualizar os efeitos no modelo.")

# Sliders para parâmetros
s = st.slider("Taxa de Poupança (s)", 0.01, 0.8, 0.3, 0.01)
n = st.slider("Taxa de Crescimento Populacional (n)", 0.001, 0.1, 0.02, 0.001)
d = st.slider("Taxa de Depreciação (d)", 0.001, 0.1, 0.02, 0.001)
alpha = st.slider("Participação do Capital (α)", 0.1, 0.9, 0.3, 0.01)

# Geração dos dados
k_vals = np.linspace(0.005, 100, 200)
y_vals, sy_vals, dep_vals, c_vals = update_curves(k_vals, s, n, d, alpha)
k_star, y_star, c_star, w_star, r_star = find_steady_state(s, n, d, alpha)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(k_vals, y_vals, 'b-', label='Produto por Trabalhador (y)', linewidth=2)
ax.plot(k_vals, sy_vals, 'g-', label='Investimento Efetivo (sy)', linewidth=2)
ax.plot(k_vals, dep_vals, 'r-', label='Investimento Necessário (n+d)k', linewidth=2)
ax.plot(k_vals, c_vals, color='orange', label='Consumo por Trabalhador (c)', linewidth=2)
ax.axvline(k_star, color='gray', linestyle='--', label='k* (Estado Estacionário)')
ax.plot(k_star, y_star, 'ko', label='Ponto de Estado Estacionário')
ax.set_xlabel('Estoque de Capital por Trabalhador (k)')
ax.set_ylabel('Produto por Trabalhador (y)')
ax.set_title('Curvas do Modelo de Solow')
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Exibição dos valores de equilíbrio
st.subheader("🔍 Parâmetros e Estado Estacionário")
st.text(f"s = {s:.2f} | n = {n:.3f} | d = {d:.3f} | alpha = {alpha:.2f}")
st.text(f"k* = {k_star:.3f} | y* = {y_star:.3f} | c* = {c_star:.3f}")
st.text(f"w* = {w_star:.3f} | r* = {r_star:.3f}")
