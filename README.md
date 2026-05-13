On this Repo I am going to go through all the basics / intermediate / advanced protocols, software, hardware & tricks about OT applied Cybersecurity which is already vital for a country's indepence.

Technologies that I will go through:
• OS: Ubuntu (Analyser), Windows 11 (Victim), Kali Linux (Attacker)
• MQTT · Zigbee · Wireshark / Laboratorio inicial 
• Wazuh · ELK · Zeek /  Detección de amenazas
• IEC 62443 · Modbus · SCADA · NIS2 / Arquitectura de planta solar
• Raspberry Pi / Servidor Local

El proyecto va a constar de 6 fases
  • FASES DE APRENDIZAJE
  
FASE 1 - 2 ·
Protocolos IoT y Laboratorio Base
■ MQTT — empieza aquí (es el más usado y el más inseguro)
· Instala broker Mosquitto en local (gratuito)
· Captura tráfico con Wireshark + plugin MQTT
· Practica con mqtt-pwn para entender vectores de ataque
■ Zigbee / Z-Wave — domótica e edificios
· Compra dongle USB Zigbee CC2531 (~15–20€)
· Captura y analiza tramas con Wireshark + plugin Zigbee
■ Raspberry Pi como servidor de laboratorio
· Instala Raspberry Pi 4 (~60–80€) como nodo central del lab
· Corre servicios IoT y simula dispositivos conectados
■ Hardware: aprovecha tu ventaja
· Identifica puertos UART en placas baratas de segunda mano
· Conéctate por puerto serie para obtener logs del dispositivo
· Extrae firmware de un dispositivo con binwalk (gratuito)
---------------------------------------------------------------
FASE 2 - 4 •
SIEM, Blue Team y Detección de Amenazas
■ Wazuh — SIEM open source (gratuito)
· Descarga la imagen lista para importar en VirtualBox/VMware
· Conecta agentes a tus dispositivos IoT del laboratorio
· Crea reglas de detección personalizadas para tráfico MQTT anómalo
■ Elastic Stack (ELK) — el más usado en empresas
· Monta tu propio stack: Elasticsearch + Logstash + Kibana
· Crea dashboards de monitoreo de dispositivos IoT
· Aprende a escribir queries en KQL (Kibana Query Language)
■ Zeek (antes Bro) — análisis de tráfico de red
· Instala Zeek y apúntalo al tráfico de tu red de laboratorio
· Crea scripts básicos para detectar conexiones IoT sospechosas
■ Ejercicio integrador clave
· Monta red con dispositivos IoT reales + Wazuh activo
· Genera tráfico normal y tráfico de ataque simulado
· Documenta el proceso completo: detección → análisis → respuesta
---------------------------------------------------------------
FASE 3 - 4 •
OT Security y Sector Fotovoltaico
■ IEC 62443 — el estándar clave que te diferencia
· Estudia la arquitectura de zonas y conductos (Zones & Conduits)
· Entiende los niveles de seguridad SL-1 a SL-4
· Descarga el resumen gratuito de ISAGCA (ISA Global Cybersecurity Alliance)
■ Protocolos industriales fotovoltaicos
· Modbus TCP/RTU — el más usado en inversores solares, sin cifrado nativo
· DNP3 — común en sistemas SCADA de distribución eléctrica
· Sunspec — protocolo específico para monitoreo de plantas solares
■ Arquitectura de una planta fotovoltaica
· Inversores → Gateway de comunicación → SCADA → Red corporativa
· Entiende dónde están los puntos de entrada para un atacante
· Estudia el caso Colonial Pipeline como ejemplo de ataque OT real
■ SCADA simulado en laboratorio
· Instala OpenPLC + GNS3 para simular entorno industrial básico
· Simula comunicación Modbus entre PLC virtual e inversor
■ NIS2 aplicada al sector energético
· Lee el FAQ de NIS2 de INCIBE (gratuito en incibe.es)
· Entiende qué obligaciones tienen las empresas fotovoltaicas
· Aprende los conceptos: gestión de riesgos, notificación de incidentes, cadena de suministro
---------------------------------------------------------------
FASE 4 - 5 •
Certificación CompTIA Security+ (SY0-701)
■ Por qué Security+ y no otra
· Es la certificación junior más reconocida por empleadores en España
· Cubre exactamente lo que necesitas: redes, amenazas, criptografía, respuesta a incidentes
· Coste del examen: ~350€ (busca vouchers con descuento en CompTIA.com)
■ Material de estudio recomendado (todo accesible)
· Professor Messer — curso gratuito completo en YouTube (el mejor recurso)
· Jason Dion en Udemy — ~15€ en oferta, incluye práctica con simulador de examen
· ExamCompass.com — tests de práctica gratuitos ilimitados
■ Metodología de estudio
· Semanas 1–3: estudia por dominios (ataques, arquitectura, implementación...)
· Semana 4: solo exámenes de práctica hasta superar el 85% consistentemente
· Semana 5–6: examen real
■ Resultado esperado
· Certificación reconocida internacionalmente que valida tus conocimientos
· Ironhack la incluye gratis en su bootcamp — tú la consigues por 350€ sin bootcamp
---------------------------------------------------------------
Fase 5 - 6 •
Construir Credibilidad Pública
■ GitHub — tu portfolio técnico
· Repositorio principal: "iot-ot-security-lab" con toda la arquitectura documentada
· README detallado: qué montaste, qué aprendiste, qué detectaste
· Incluye diagramas de red, capturas de Wireshark anonimizadas, reglas Wazuh creadas
· Scripts propios aunque sean simples (detección de MQTT sin autenticación, etc.)
■ Write-ups técnicos — 2 a 3 artículos en 6 meses
· "Analicé el tráfico de un enchufe Tuya y esto encontré" → Medium o blog propio
· "Cómo monté un laboratorio de seguridad IoT con Wazuh por menos de 200€"
· "NIS2 y el sector fotovoltaico: qué deben hacer las empresas y por qué importa"
■ LinkedIn técnico — no curricular
· Publica lo que aprendes cada semana (1–2 posts semanales)
· Formato: "Hoy aprendí X sobre seguridad Modbus. Lo que descubrí fue..."
· Conecta con profesionales de S21sec, Tarlogic, Dragos en España
· Únete a grupos: ISACA Spain, CCN-CERT community, Ciberseguridad Industrial
■ Networking activo desde el mes 3
· Mensaje directo a 2–3 analistas OT por semana en LinkedIn
· No pidas trabajo: pide 15 minutos para entender cómo entraron ellos
· Asiste a eventos gratuitos: webinars de INCIBE, ISACA Spain, S21sec
---------------------------------------------------------------




