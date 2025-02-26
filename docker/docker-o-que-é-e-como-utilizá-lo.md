# Docker: o que é e como utilizá-lo?

Date: 2020-06-17 14:47:32

Categories: Docker

---

<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1003" src="http://solucoesms.com.br/wp-content/uploads/2020/06/docker.jpg" alt="" width="750" height="422" srcset="https://solucoesms.com.br/wp-content/uploads/2020/06/docker.jpg 750w, https://solucoesms.com.br/wp-content/uploads/2020/06/docker-300x169.jpg 300w" sizes="auto, (max-width: 750px) 100vw, 750px" /></p>
<p style="text-align: justify;">Se você utiliza máquinas virtuais para testar seus sistemas e acha que pode fazer algo com um pouco menos de recursos, você pensou certo! O Docker veio para o mercado para mostrar que isso é possível.</p>
<h2>Mas antes de tudo, o que é o Docker?</h2>
<p style="text-align: justify;">De forma resumida, o Docker é uma plataforma de código aberto, desenvolvido na linguagem Go e criada pelo próprio Google. Por ser de alto desempenho, o software garante maior facilidade na criação e administração de ambientes isolados, garantindo a rápida disponibilização de programas para o usuário final.</p>
<h2>Quais são as funcionalidades do Docker?</h2>
<p style="text-align: justify;">O Docker tem como objetivo criar, testar e implementar aplicações em um ambiente separado da máquina original, chamado de container. Dessa forma, o desenvolvedor consegue empacotar o software de maneira padronizada. Isso ocorre porque a plataforma disponibiliza funções básicas para sua execução, como: código, bibliotecas, runtime e ferramentas do sistema.</p>
<h2>Quais são os benefícios do Docker?</h2>
<p style="text-align: justify;">A grande vantagem no uso da plataforma é a rapidez em que o software pode ser disponibilizado — em uma frequência até 7 vezes mais rápida do que a virtualização convencional. Outro benefício oferecido pela plataforma é a possibilidade de configurar diferentes ambientes de forma rápida, além de diminuir o número de incompatibilidades entre os sistemas disponíveis.</p>
<h2>Como instalar o docker?</h2>
<p style="text-align: justify;">Temos que fazer algumas modificações para garantir que o docker consiga ser executado com tranquilidade no seu equipamento, para isso siga os passos abaixo:</p>
<p><strong>1 &#8211; Download do WSL 1:</strong></p>
<p style="text-align: justify;">O WSL 2 é um componente do windows que habilita a funcionalidade de se utilizar o Linux no shell do Windows. Execute o seguinte comando para sua execução e habilitação:</p>
<pre>dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart</pre>
<p><strong>2- Atualize para o WSL 2:</strong></p>
<pre>dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart</pre>
<p><strong>3- Defina o WSL 2 como padrão:</strong></p>
<pre>wsl --set-default-version 2</pre>
<p><strong>4- Download do Docker</strong></p>
<p style="text-align: justify;">Primeiramente, faça o download do software no site oficial <a href="https://hub.docker.com/editions/community/docker-ce-desktop-windows/">https://hub.docker.com/editions/community/docker-ce-desktop-windows/</a> ou <a href="https://docs.docker.com/docker-for-windows/install/">https://docs.docker.com/docker-for-windows/install</a>. Ao iniciar a instalação do pacote, ele perguntará sobre a ativação do WSL 2 que é a possibilidade de utilizar comandos linux no shell do Windows assim como informado acima. Aceite e aguarde até o final.</p>
<p><strong>5- Ativação do Docker</strong></p>
<p>Execute as seguintes opções para configuração do ambiente:</p>
<p style="padding-left: 40px;">a) Vá no menu Iniciar &gt; Executar &gt; Docker Desktop</p>
<p style="padding-left: 40px;">b) Na barra de tarefas, clique sobre o ícone do Docker (uma baleia) e em Settings</p>
<p style="padding-left: 40px;">c) Clique em Expose deamon on tcp://localhost:2375 without TLS &gt; Apply</p>
<p>Pronto! seu Docker está ativo e em funcionamento. No próximo post falarei sobre como gerenciá-lo e como criar e importar dados para seu novo ambiente.</p>
<p>Enjoy!</p>
