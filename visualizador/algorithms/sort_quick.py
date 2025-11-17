# =============================
# QuickSort paso a paso (Corregido)
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
# =============================

items = []
n = 0

# Estado
stack = []          # Pila de (inicio, fin)
i = 0               # Puntero para partición
j = 0               # Puntero para partición
pivot = None        # Valor del pivote (no usado directamente, pero mantenido)
phase = "idle"      # idle, partitioning, pushing
low = 0             # Inicio del rango actual
high = 0            # Fin del rango actual

def init(vals):
    global items, n, stack, i, j, pivot, phase, low, high
    items = list(vals)
    n = len(items)

    # Reiniciar todo
    stack = []
    if n > 1:
        stack.append((0, n - 1))  # Primer rango
    phase = "idle"
    i = 0
    j = 0
    pivot = None
    low = 0
    high = 0

def step():
    global items, stack, i, j, pivot, phase, low, high

    # Si no queda nada por ordenar y estamos en idle
    if not stack and phase == "idle":
        return {"done": True}

    # Tomamos el rango actual
    if phase == "idle":
        if not stack:
            return {"done": True}
        low, high = stack.pop()
        if low >= high:
            # Rango trivial, continuar
            phase = "idle"
            return {"a": 0, "b": 0, "swap": False, "done": False}
        pivot = items[high]  # Pivote es el último elemento
        i = low - 1
        j = low
        phase = "partitioning"

    # -----------------------------
    # FASE: partitioning
    # -----------------------------
    if phase == "partitioning":
        if j <= high - 1:
            swap_happened = False
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                swap_happened = True
            j += 1
            return {"a": i, "b": j - 1, "swap": swap_happened, "done": False}
        else:
            # Intercambiar el pivote al lugar correcto
            items[i + 1], items[high] = items[high], items[i + 1]
            phase = "pushing"
            return {"a": i + 1, "b": high, "swap": True, "done": False}

    # -----------------------------
    # FASE: pushing — empujar subrangos
    # -----------------------------
    if phase == "pushing":
        pivot_index = i + 1  # Posición final del pivote

        # Subrango izquierdo
        if low < pivot_index:
            stack.append((low, pivot_index - 1))

        # Subrango derecho
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

        phase = "idle"
        return {"a": 0, "b": 0, "swap": False, "done": False}

    return {"done": True}
