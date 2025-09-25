# 📊 DASHBOARD COMUNITARIO IZA - AUTOACTUALIZABLE

## 📈 ESTADÍSTICAS EN TIEMPO REAL
- **👥 Usuarios únicos registrados:** 1
- **📊 Total de interacciones:** 1
- **🕒 Última actualización:** $(date)

## 👤 USUARIOS ACTIVOS
1. **token-10-protocol** - Primer acceso: 2025-09-25 21:51:31

## 📅 ACTIVIDAD RECIENTE
- 2025-09-25 21:51:31 - token-10-protocol dio STAR al repositorio

## 🎯 PRÓXIMOS OBJETIVOS
- [ ] 5 usuarios únicos
- [ ] 20 interacciones totales
- [ ] Primer usuario externo
      - name: 📊 ACTUALIZAR DASHBOARD
        run: |
          # Contar métricas
          TOTAL_EVENTOS=$(cat data/analitica/accesos.jsonl | wc -l)
          USUARIOS_UNICOS=$(cat data/analitica/accesos.jsonl | jq -r '.usuario' | sort | uniq | wc -l)
          ULTIMO_EVENTO=$(tail -1 data/analitica/accesos.jsonl | jq -r '.fecha')
          
          # Crear/actualizar dashboard
          cat > data/dashboard.md << EOF
# 📊 DASHBOARD COMUNITARIO IZA - AUTOACTUALIZABLE

## 📈 ESTADÍSTICAS EN TIEMPO REAL
- **👥 Usuarios únicos registrados:** $USUARIOS_UNICOS
- **📊 Total de interacciones:** $TOTAL_EVENTOS
- **🕒 Última actualización:** $(date)

## 👤 USUARIOS ACTIVOS
$(cat data/analitica/accesos.jsonl | jq -r '.usuario' | sort | uniq | awk '{print "1. **" $1 "** - Primer acceso: [por calcular]"}' | head -5)

## 📅 ACTIVIDAD RECIENTE (últimas 5)
$(cat data/analitica/accesos.jsonl | tail -5 | jq -r '" - \(.fecha) - \(.usuario) - \(.evento)"')

## 🎯 PRÓXIMOS OBJETIVOS
- [ ] 5 usuarios únicos
- [ ] 20 interacciones totales  
- [ ] Primer usuario externo
EOF
          
          echo "✅ Dashboard actualizado"
