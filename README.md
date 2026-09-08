# Desarrollo de una API REST para gestión de cuentas bancarias

La institución financiera necesita una API REST para gestionar las cuentas de sus clientes. La API debe permitir la creación, lectura, actualización y eliminación de cuentas. Los datos de las cuentas se almacenarán en una base de datos relacional. Los actores involucrados son el cliente, el sistema de gestión de cuentas y el sistema de auditoría. La API debe ser idempotente en la creación de cuentas y manejar errores comunes como cuentas duplicadas o datos inválidos. La latencia máxima permitida para las operaciones es de 200ms.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Desarrollo de API REST en banca utilizando FastAPI y SQLAlchemy |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de endpoints y modelos de datos

**Objetivo:** Definir los endpoints necesarios y los modelos de datos para la gestión de cuentas bancarias.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los endpoints necesarios para crear, leer, actualizar y eliminar cuentas.
- Definir los modelos de datos para las cuentas, incluyendo atributos como número de cuenta, saldo, tipo de cuenta y cliente asociado.
- Asegurar que la API sea idempotente en la creación de cuentas y maneje correctamente los errores de cuentas duplicadas.

**Entregable:** Documento que describa los endpoints y modelos de datos, incluyendo las consideraciones de idempotencia y manejo de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los diferentes tipos de cuentas que puede tener un cliente (corriente, ahorro, etc.)
- Piensa en los atributos necesarios para identificar de forma única una cuenta.

</details>

### Fase 2: Implementación de la lógica de negocio

**Objetivo:** Implementar la lógica de negocio para los endpoints definidos, incluyendo la validación de datos y el manejo de errores.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar la lógica de negocio para los endpoints de creación, lectura, actualización y eliminación de cuentas.
- Validar los datos de entrada para asegurar que cumplen con los requisitos de negocio (por ejemplo, saldo positivo, número de cuenta válido).
- Manejar los errores comunes, como cuentas duplicadas o datos inválidos, de forma adecuada.

**Entregable:** Código que implementa la lógica de negocio para los endpoints definidos, incluyendo la validación de datos y el manejo de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los diferentes escenarios de error que pueden ocurrir al crear o actualizar una cuenta.
- Piensa en cómo comunicar de forma clara los errores al cliente.

</details>

### Fase 3: Integración con la base de datos

**Objetivo:** Integrar la API con la base de datos para el almacenamiento y recuperación de datos de las cuentas.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Configurar la conexión a la base de datos utilizando SQLAlchemy.
- Implementar las operaciones CRUD (Create, Read, Update, Delete) para las cuentas en la base de datos.
- Asegurar que las operaciones sean atómicas y consistentes.

**Entregable:** Código que integra la API con la base de datos, incluyendo las operaciones CRUD para las cuentas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de transacciones para asegurar la atomicidad y consistencia de las operaciones.
- Piensa en cómo manejar las posibles fallas de la base de datos.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los endpoints y modelos de datos en el contexto de una API REST?
- **paraQueSirve**: ¿Para qué sirven los endpoints y modelos de datos en una API REST?
- **comoSeUsa**: ¿Cómo se implementa la lógica de negocio en una API REST?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al crear o actualizar una cuenta en una API REST y cómo se manejan?

## Criterios de Evaluacion

- Definición clara y completa de endpoints y modelos de datos.
- Implementación correcta de la lógica de negocio, incluyendo validación de datos y manejo de errores.
- Integración exitosa de la API con la base de datos, incluyendo operaciones CRUD atómicas y consistentes.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
