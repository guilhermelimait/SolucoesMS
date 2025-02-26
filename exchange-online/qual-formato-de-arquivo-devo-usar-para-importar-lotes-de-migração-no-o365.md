# Qual formato de arquivo devo usar para importar lotes de migração no O365?

Date: 2020-03-02 12:32:41

Categories: Exchange, Exchange Online, O365, Office 365

---

<p style="text-align: justify;">Sempre gosto de compartilhar algumas informações que podem ajudar aos administradores de ambiente a executarem melhor suas tarefas, ou até mesmo para mim mesmo num futuro onde eu precise novamente desse tipo de informação. Por isso mesmo, gostaria de compartilhar que os arquivos que são utilizados para importação de dados de emails dos usuários do Exchange Online do O365. Cada origem poderá ser diferente, por isso mesmo, indico abaixo formatos que podem ser utilizados em cada tipo de situação. A fonte original sempre será a própria Microsoft, porém, esses formatos abaixo até a data de publicação desse post já foram utilizados em vários projetos e complexidades diferentes.</p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-939" src="http://solucoesms.com.br/wp-content/uploads/2020/02/71b69cf1e4fb4e905523a717e0e78113.jpeg" alt="" width="577" height="130" srcset="https://solucoesms.com.br/wp-content/uploads/2020/02/71b69cf1e4fb4e905523a717e0e78113.jpeg 577w, https://solucoesms.com.br/wp-content/uploads/2020/02/71b69cf1e4fb4e905523a717e0e78113-300x68.jpeg 300w" sizes="auto, (max-width: 577px) 100vw, 577px" /></p>
<p><strong>Fonte:</strong> Gsuite<br />
<strong>Situação:</strong> Todos os usuários do Gsuite possuem apenas um endereço principal, nenhum outro endereço é usado.<br />
<strong>Formato do arquivo:</strong> CSV<br />
<strong>Exemplo do arquivo:</strong> Apenas o campo com o endereço de email do usuário precisa ser informado.</p>
<pre class="brush: plain; title: ; notranslate" title="">EmailAddress 
usuario@dominioprincipal.com.br</pre>
<p>&nbsp;</p>
<hr />
<p><strong>Fonte:</strong> Gsuite<br />
<strong>Situação:</strong> A <span style="color: #ff0000;">MAIORIA</span> dos usuários do Gsuite possuem um endereço principal mas vários deles possuem domínios principais diferentes, o domínio principal da companhia pode ser um secundário da empresa.<br />
<strong>Formato do arquivo:</strong> CSV<br />
<strong>Exemplo do arquivo:</strong> abaixo</p>
<pre class="brush: plain; title: ; notranslate" title="">EmailAddress,UserName 
usuario@dominioprincipalquevaificarnamicrosoft.com.br,usuario@dominioqueousuariofazlogonnoGsuite.com.br</pre>
<p><strong>Exemplo2:</strong> O usuário vai receber o solucoesms.com.br como endereço primário na microsoft, enquanto o usuário usa o formato sms.com no Gsuite.</p>
<pre class="brush: plain; title: ; notranslate" title="">Emailaddress,Username 
Guilherme@solucoesms.com.br,guilherme.lima@sms.com</pre>
<hr />
<p><strong>Fonte:</strong> Zimbra<br />
<strong>Situação:</strong> Importação dos dados do usuário com direito administrativo nas contas.<br />
<strong>Formato do arquivo:</strong> CSV<br />
<strong>Exemplo do arquivo:</strong> abaixo</p>
<pre class="brush: plain; title: ; notranslate" title="">EmailAddress,UserName,Password
emaildousuario01@dominio.com.br,#emaildousuario01@dominio.com.br#Admin@dominio.com.br#,SenhaDoAdmin emaildousuario02@dominio.com.br,#emaildousuario02@dominio.com.br#Admin@dominio.com.br#,SenhaDoAdmin emaildousuario03@dominio.com.br,#emaildousuario03@dominio.com.br#Admin@dominio.com.br#,SenhaDoAdmin emaildousuario04@dominio.com.br,#emaildousuario04@dominio.com.br#Admin@dominio.com.br#,SenhaDoAdmin emaildousuario05@dominio.com.br,#emaildousuario05@dominio.com.br#Admin@dominio.com.br#,SenhaDoAdmin</pre>
<p>&nbsp;</p>
