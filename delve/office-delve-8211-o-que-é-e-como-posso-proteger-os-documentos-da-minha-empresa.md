# Office Delve &#8211; o que é e como posso proteger os documentos da minha empresa?

Date: 2019-08-06 17:05:04

Categories: Delve, O365, OneDrive, Sharepoint, Skype, Teams, Yammer

---

<p><img loading="lazy" decoding="async" class="aligncenter wp-image-865 size-large" src="http://solucoesms.com.br/wp-content/uploads/2019/08/delve1-1024x604.png" alt="" width="678" height="400" srcset="https://solucoesms.com.br/wp-content/uploads/2019/08/delve1-1024x604.png 1024w, https://solucoesms.com.br/wp-content/uploads/2019/08/delve1-300x177.png 300w, https://solucoesms.com.br/wp-content/uploads/2019/08/delve1-768x453.png 768w, https://solucoesms.com.br/wp-content/uploads/2019/08/delve1.png 1025w" sizes="auto, (max-width: 678px) 100vw, 678px" /></p>
<p style="text-align: justify;">Se você está lendo esse artigo é porque está realmente interessado em saber o que o <em>Office 365</em> está trazendo de novidades para sua empresa e para entender o que essas mudanças podem fazer para impactar ou disponibilizar no seu ambiente.</p>
<p style="text-align: justify;">O <em><strong>Delve</strong> </em>&#8211; que significa mergulhar, ir à fundo &#8211; nosso tema de hoje, é a evolução do <em>Office Graph</em>, uma ferramenta que monitora o seu acesso à documentos através do <em>Sharepoint</em>, <em>OneDrive</em>, <em>Skype</em>, <em>Yammer</em>, <em>Teams</em> e anexos de emails e que irá apresentar os documentos que são mais relevantes para você por uma interface no portal do O365. Bem profundo não é mesmo?</p>
<h2 style="text-align: justify;">Já está confuso?</h2>
<p style="text-align: justify;">Não se preocupe, vamos com calma e usando de alguns exemplos para clarificar:</p>
<ul style="text-align: justify;">
<li style="text-align: justify;">Um gerente do departamento financeiro envia um relatório de vendas para seus funcionários por email. Esse documento ficará disponível automaticamente pelo <em>Delve</em> para todos eles. Se esse mesmo relatório for compartilhado com o departamento de marketing por exemplo, para verificar campanhas de vendas, ele estará então sendo passível de acesso por <strong>todos</strong> do departamento de Marketing e Vendas.</li>
<li>Um funcionário do departamento de logística que tem acesso à todos os documentos de sua área é transferido para executar outra função em outro departamento. Como geralmente as empresas se esquecem de fazer a alteração de seus dados no <em>Active Directory</em> e o fazem apenas no sistema de RH, o usuário continua tendo acesso às informações do antigo departamento e do novo.</li>
</ul>
<p style="text-align: justify;">Perigoso? De certa forma sim! Devido ao uso comum de compartilhamento de informações diretamente por email e não pelo <em>Sharepoint</em> para controle de acesso, esses dados acabam ficando cada vez mais passíveis de serem acessados por usuários não autorizados.</p>
<p style="text-align: justify;">Por padrão, o <em>Delve</em> irá utilizar do meio mais simples que temos para saber se alguém faz parte do mesmo departamento ou grupo, ele irá verificar como os campos de Gerente, Cidade, Departamento e Companhia estão preenchidos. Se o padrão da sua empresa é deixá-los em branco, o perigo de vazamento de dados é iminente. Fique atento!</p>
<h2>Mas existe alguma forma de me proteger ou proteger a minha empresa?</h2>
<p>Sim, há! Acompanhe abaixo três soluções simples que já podem ser realizadas no seu ambiente.</p>
<ul>
<li><strong>Oculte documentos específicos ou uma pasta completa do Delve<br />
</strong>No <em>Sharepoint</em> existe uma propriedade chamada <em>HiddenFromDelve</em> que deve ser habilitada para ocultar apenas os documentos selecionados, para tal faça o seguinte:</p>
<ul>
<li>Nas opções da <em>Library</em> que quiser efetuar essa ação, adicione uma coluna com o texto <em><strong>HideFromDelve</strong></em> sem espaços e do tipo &#8220;<em>yes/no</em>&#8220;</li>
<li>Para cada documento apresentado na pasta que você quiser ocultar para terceiros, clique na propriedade <em><strong>Yes</strong></em>.</li>
<li>Se quiser ocultar de todos os documentos de uma vez, selecione a opção <em><strong>Yes</strong> </em>como padrão.</li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;"><em>Obs.: Os documentos estarão ocultos para o Delve, mas não para pesquisas feitas no Sharepoint.</em></li>
</ul>
<ul>
<li><strong>Oculte toda uma biblioteca de documentos do <em>Search</em> e <em>Delve<br />
</em></strong>Acesse o portal <a href="http://delve.office.com">delve.office.com</a></p>
<ul>
<li>Clique no ícone da engrenagem</li>
<li>Desmarque a opção na aba <em>Documentos</em>, deixe-a <em><strong>Desativada</strong></em>.</li>
<li>Clique em <em>OK</em> para salvar a alteração.</li>
</ul>
</li>
</ul>
<p><img loading="lazy" decoding="async" class="aligncenter wp-image-866 size-large" src="http://solucoesms.com.br/wp-content/uploads/2019/08/delve2-1024x680.png" alt="" width="678" height="450" srcset="https://solucoesms.com.br/wp-content/uploads/2019/08/delve2-1024x680.png 1024w, https://solucoesms.com.br/wp-content/uploads/2019/08/delve2-300x199.png 300w, https://solucoesms.com.br/wp-content/uploads/2019/08/delve2-768x510.png 768w, https://solucoesms.com.br/wp-content/uploads/2019/08/delve2.png 1047w" sizes="auto, (max-width: 678px) 100vw, 678px" /></p>
<blockquote><p><em>Obs.: Essa opção irá ocultar a pasta para pesquisa tanto no Delve quanto no Search.</em></p></blockquote>
<ul>
<li><strong>Oculte o site completamente do Search e Delve<br />
</strong>Acesse o portal do <em>OneDrive</em></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li>Clique na engrenagem do lado direito superior</li>
<li>Clique em <em>OneDrive Settings</em></li>
<li>Clique em <em>More Settings</em> no menu esquerdo</li>
<li>Clique em <em>Return</em> <em>to the old Site settings page</em></li>
<li>Clique em <em>Search</em> and <em>Offline Availability</em></li>
<li>Marque a opção <strong><em>No</em> </strong>em <em>Indexing Site Content</em></li>
</ul>
</li>
</ul>
<p><img loading="lazy" decoding="async" class="aligncenter size-large wp-image-867" src="http://solucoesms.com.br/wp-content/uploads/2019/08/onedrive1-1024x253.png" alt="" width="678" height="168" srcset="https://solucoesms.com.br/wp-content/uploads/2019/08/onedrive1-1024x253.png 1024w, https://solucoesms.com.br/wp-content/uploads/2019/08/onedrive1-300x74.png 300w, https://solucoesms.com.br/wp-content/uploads/2019/08/onedrive1-768x189.png 768w, https://solucoesms.com.br/wp-content/uploads/2019/08/onedrive1.png 1042w" sizes="auto, (max-width: 678px) 100vw, 678px" /></p>
<blockquote><p><em>Obs.: Essa opção irá bloquear o compartilhamento de pastas e arquivos no Delve, Sharepoint e no OneDrive.</em></p></blockquote>
<h2>Conclusão</h2>
<p style="text-align: justify;">O<strong><em> Delve </em></strong>veio para deixar o acesso às informações corporativas de forma mais simples e acessíveis para os usuários tornando-se a ferramenta mais poderosa até então no compartilhamento de dados da Microsoft. Porém, para que possa ser bem utilizada, tanto os usuários quanto os administradores devem estar preparados para realizar ações constantes de mapeamento e auditorias do ambiente. A educação e entendimento das ferramentas informadas aqui são imprescindíveis para que as empresas tenham controle e segurança sobre seus dados.</p>
<p>Gostou desse material? Compartilhe! Mais administradores e usuários precisam saber sobre ela!<br />
Grande abraço!</p>
<p style="text-align: justify;">Fonte1: <a href="https://docs.microsoft.com/pt-br/sharepoint/delve-for-office-365-admins">https://docs.microsoft.com/pt-br/sharepoint/delve-for-office-365-admins</a><br />
Fonte2: <a href="https://support.office.com/pt-br/article/como-o-office-delve-reconhece-o-que-%C3%A9-relevante-para-mim-048d502e-80a7-4f77-ac5c-f9d81733c385">https://support.office.com/pt-br/article/como-o-office-delve-reconhece-o-que-%C3%A9-relevante-para-mim-048d502e-80a7-4f77-ac5c-f9d81733c385</a></p>
