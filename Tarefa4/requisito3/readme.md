# Requisito 3 — Segunda parte da análise

| Rede | No. Vertex | No. Edges | Degree assortativity | No. Connected components | Giant component size | Avg. clustering coef. |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 15676 | 1953297 | 0.5787544969461272 | 187 | 14244 | 0.9073239911818288 |
| 7 | 1913 | 7424 | -0.010260050126892737 | 106 | 895 | 0.8838263415888769 |
| 15 | 5532 | 889090 | 0.4871596928304268 | 72 | 5010 | 0.930478877882558 |
| 17 | 874 | 5553 | 0.9302314584096364 | 98 | 192 | 0.9217832802651343 |

Começando pelo tamanho das redes, temos o objetivo 3 com o maior número de autores (nós) — os artigos de muitíssimos autores já davam essa impressão, e poderíamos levar a crer que a quantidade de artigos também influencia, tendo a rede 3 a maior de todas, com 3180.

Essa hipótese, entretanto, desmantela-se diante dos resultados das demais redes. A rede do objetivo 17, com 3110 artigos, apresenta a menor quantidade de autores, tendo cerca de metade do que o objetivo 7, que tem aproximadamente 34% (1055) dos artigos; e quase 16% dos autores do objetivo 15, que possui 20% (624) de sua quantia de artigos.

Juntando estes dados ao número de arestas, conseguimos comparar a densidade das redes — onde percebe-se uma esparsidão maior na rede 7, contribuíndo à ideia de cooperações mais limitadas. Apesar do maior número de vértices, a rede 3 manteve densidade próxima à rede 17. Este resultado, bem como a maior densidade da rede 15 , são atribuíveis aos já mencionados artigos de muitos autores, que formaram os "outliers" no requisito 2.

Com o coeficiente de assortatividade temos um resultado bem mais visível para o comportamento das redes: o comportamento da rede 7 contrasta com a assortatividade esperada, reforçando a ideia de pequenas comunidades pouco interligadas. Ao juntar com as informações de componentes conectados — onde tem-se um alto número de componentes conectados em relação ao número de vértices — esta concepção é reforçada.

Analisando de forma similar a rede 17, consegue-se atribuir a alta assortatividade com grandes hubs, supostamente atrelados a diferentes áreas do conhecimento, desconectados — gerando este número maior de componentes conectados por nó. As redes 3 e 15 apresentam comportamentos semelhantes, potencialmente pela mesma causa, mas podemos verificar diferenças na quantia de componentes conectados por nó e quantia de amostras de artigos.

O GCC nos permite observar um pouco como podem ser feitas as conexões entre hubs e o tamanho dos demais componentes conectados. As redes 3 e 15 possuem GCCs grandíssimos em relação ao número de nós, o que implica num tamanho médio das demais componentes conectadas ínfimo — onde, agregado ao menor tamanho da rede 15, também reflete sua assortatividade menor que a da rede 3. O GCC pequeno da rede 17 reforça a hipótese de hubs para diferentes áreas científicas, enquanto que o da rede 7 pode ser induzido à conexão entre hubs ser como "o homem da caverna selecionado aleatoriamente" na figura de alguém que entra em outro projeto ou pela existência de nós que, por alguma propriedade não modelada, façam esta ligação — como gestores operando em um alto nível.

O coeficiente de clustering, apesar de alto, não é incomum a modelos de mundo pequeno como o inferido à rede 7, mas também pode ser causado por grandes comunidades, como no resto.

Por fim, restam questionamentos do quanto a rede 7 poderia se interligar mais apesar de sua natureza, à exemplo da rede 17, e se uma melhor filtragem dos dados é necessária para artigos anômalos.


(Parei de contar a partir daqui)  
Contado com o wordcounter.net (499 palavras)  
Tabela extra de dados mencionados:
|Rede | Total de Artigos | Densidade | "Sobra do GCC" |
| --- | ---| --- | --- |
| 3 | 3180 | 0.0158984752 | 1432 |
| 7 | 1055 | 0.00405943041 | 1018 |
| 15 | 624 | 0.0581152207 | 522 |
| 17 | 3110 | 0.014555663 | 682 |