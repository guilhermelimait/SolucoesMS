# Como fazer resize de uma VM no Azure?

Date: 2020-11-24 20:20:55

Categories: Azure

---

<p style="text-align: justify;">Após uma nova demanda e compartilhamento entre amigos, surgiu mais uma oportunidade de compartilhar conceitos simples e que podem agregar no dia a dia dos especialistas ou analistas em TI. Nesse tópico de hoje, tivemos como início a discussão sobre como fazer para fazer um resize ou método para aumento ou diminuição de uma máquina virtual que esteja hospedada na Azure.</p>
<p style="text-align: justify;">Primeiramente, você conhece a <a href="https://azure.microsoft.com/pt-br/pricing/calculator/" target="_blank" rel="noopener noreferrer">calculadora</a> de máquinas virtuais da Azure? É à partir dela que tudo se inicia, já que de acordo com o tamanho do servidor ou máquina que você está criando que ela será cobrada. Quanto maior a demanda, maior o valor. Existem várias técnicas de gestão de criação desses equipamentos, mas hoje vamos falar apenas em como fazê-lo ok?</p>
<p style="text-align: justify;">Imagine então que você possui um equipamento e que após algumas métricas usando o Azure Metrics, você percebeu que existem alguns gargalos, seja de memória ou de CPU do equipamento. O que fazer? Primeiramente vá até a calculadora, verifique nela o que precisa, aumentar memória ou processador? Selecione o que precisa e veja se os novos modelos lhe cairão bem.</p>
<p><img loading="lazy" decoding="async" class="aligncenter size-large wp-image-1095" src="http://solucoesms.com.br/wp-content/uploads/2020/11/resize2-1024x576.png" alt="" width="640" height="360" srcset="https://solucoesms.com.br/wp-content/uploads/2020/11/resize2-1024x576.png 1024w, https://solucoesms.com.br/wp-content/uploads/2020/11/resize2-300x169.png 300w, https://solucoesms.com.br/wp-content/uploads/2020/11/resize2-768x432.png 768w, https://solucoesms.com.br/wp-content/uploads/2020/11/resize2.png 1280w" sizes="auto, (max-width: 640px) 100vw, 640px" /></p>
<p style="text-align: justify;">Essa validação servirá apenas como um guia de preços, uma forma rápida de comparação de preço do equipamento por tempo de uso. Após essa primeira análise, vá até o <a href="http://portal.azure.com">http://portal.azure.com</a> e encontre o equipamento que precisa fazer a alteração de tamanho.</p>
<p style="text-align: justify;">Após identificar o que precisa, vá na VM, pare o funcionamento dela, clique em tamanho e altere para o que você precise. Após salvar o equipamento já estará no novo tamanho selecionado e você poderá iniciar o equipamento e fazer os testes para validar a melhoria no recurso. Gostou? Quer ver essa alteração em vídeo? Veja abaixo de forma bem explicada e resumida!</p>
<p><center><iframe loading="lazy" title="AZURE - Como fazer resize em VM" width="678" height="381" src="https://www.youtube.com/embed/WkCghIh50rI?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></p>
<p></center>Enjoy!</p>
