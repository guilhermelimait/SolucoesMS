# Graphical Tools estão disponíveis novamente no Powershell!

Date: 2019-08-21 11:13:52

Categories: Comando local/PC, Gerenciamento, Powershell

---

<p style="text-align: justify;">Você já se pegou em uma atividade onde precisava exportar alguns valores em um powershell mas gostaria de fazer algum tipo de filtro rápido e gerar algum resultado de forma mais simples ? Então o Graphical Tools ou GridView foram feitos pra você!</p>
<h2>Instalação</h2>
<p style="text-align: justify;">O graphical tools ou GridView do powershell é um módulo que já existe no Windows mas que pode ser adicionado no Linux e no Mac para administração remota. Deve ser instalado à partir da linha de comando abaixo com um usuário administrador. Assim que estiver instalado, já está disponível para funcionamento.</p>
<pre>Install-Module -Name Microsoft.PowerShell.GraphicalTools</pre>
<h2>Como utilizá-lo?</h2>
<p style="text-align: justify;">Por ser uma interface gráfica baseada em <a href="http://avaloniaui.net/">Avalonia</a> , ela é de simples uso e pode ser utilizada de várias formas diferentes como demonstrado abaixo:</p>
<p style="text-align: justify;"><strong>Exemplo 1</strong> &#8211; Apresentar todos os arquivos do tipo CSV em uma pasta e organizá-los por tamanho:</p>
<pre> dir *.csv | Sort-Object -Property length -Descending | Out-GridView</pre>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-883" src="http://solucoesms.com.br/wp-content/uploads/2019/08/gridview1.png" alt="" width="450" height="409" srcset="https://solucoesms.com.br/wp-content/uploads/2019/08/gridview1.png 450w, https://solucoesms.com.br/wp-content/uploads/2019/08/gridview1-300x273.png 300w" sizes="auto, (max-width: 450px) 100vw, 450px" /></p>
<p style="text-align: justify;"><strong>Exemplo 2 &#8211; </strong>Importar o conteúdo de um arquivo .csv e apresentá-lo por colunas identificadas no arquivo e separadas por um caractere delimitador:</p>
<p style="text-align: justify;">Pra esse exemplo é preciso explicar um pouco, um arquivo .csv é um arquivo que é criado com seu conteúdo identificado por colunas, e cada coluna com sua matriz ou título. Cada coluna é separada usando um caractere separador como virgula, tabulação, aspas ou qualquer outro identificado durante a sua criação. Caso esse valor não seja identificado como parâmetro, o conteúdo será apresentado todo como uma única coluna no <em>Gridview</em>. Por isso , usamos o comando de conversão de dados com o caractere delimitador. Veja abaixo:</p>
<pre>Get-Content .\validatedusers.csv | ConvertFrom-Csv -Delimiter ";" | Out-GridView</pre>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-885" src="http://solucoesms.com.br/wp-content/uploads/2019/08/gridview2.png" alt="" width="379" height="310" srcset="https://solucoesms.com.br/wp-content/uploads/2019/08/gridview2.png 379w, https://solucoesms.com.br/wp-content/uploads/2019/08/gridview2-300x245.png 300w" sizes="auto, (max-width: 379px) 100vw, 379px" /></p>
<p style="text-align: justify;"><strong>Exemplo 3</strong> &#8211; Criar um GridView para ler o conteúdo de um log enquanto ele é carregado.<br />
Sabemos que o comando de grep do linux não existe no Windows, porém existem várias formas de ser executado. Com o uso do GridView, será possível ver o conteúdo do log enquanto ele é preenchido pelo comando ou programa que o controla. Para isso use o seguinte comando:</p>
<pre class="lang-bsh prettyprint prettyprinted">Get-Content .\arquivo.log | Out-GridView -Wait</pre>
<h2>Conclusão</h2>
<p style="text-align: justify;">O Out-GridView pode ser extremamente útil para exportar e apresentar valores enquanto são carregados ou finalizados de uma forma simples e amigável, por possuir a possibilidade de ter critérios ou filtros, o seu uso é extendido ao máximo para uma pesquisa mais detalhada.</p>
<p>Espero que possa ter lhe ajudado em suas futuras buscas!</p>
<p>Fontes:<br />
<a href="https://docs.microsoft.com/pt-br/powershell/module/microsoft.powershell.utility/out-gridview?view=powershell-3.0">Microsoft </a><br />
<a href="https://www.powershellgallery.com/packages/Microsoft.PowerShell.GraphicalTools/0.2.0">Powershell Gallery</a><br />
<a href="http://avaloniaui.net/">Avalonia</a><br />
<a href="https://devblogs.microsoft.com/powershell/out-gridview-returns/">Devblogs</a></p>
