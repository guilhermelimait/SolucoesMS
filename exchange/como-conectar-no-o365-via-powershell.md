# Como conectar no O365 via powershell?

Date: 2017-05-11 18:13:50

Categories: Azure, Exchange, Office 365

---

<p style="text-align: justify;"><strong>Instalar o software necessário</strong><br />
Essas etapas precisam ser executadas apenas uma vez em seu computador e não toda vez em que você se conectar. No entanto, você provavelmente precisará instalar a versão mais recente do software periodicamente.</p>
<ol>
<li>Instale a versão de 64 bits do Assistente de Conexão do Microsoft Online Services: Assistente de Conexão do Microsoft Online Services para Profissionais de TI RTW (<a href="https://go.microsoft.com/fwlink/p/?LinkId=286152">link</a>)</li>
<li>Instalar a versão de 64 bits do Módulo Microsoft Azure Active Directory para Windows PowerShell: Módulo Microsoft Azure Active Directory para Windows PowerShell (versão de 64 bits). (<a href="https://go.microsoft.com/fwlink/p/?linkid=236297">link</a>)</li>
</ol>
<p><strong>Conectar-se ao PowerShell do Office 365</strong></p>
<p style="text-align: justify;">O Office 365 PowerShell permite que você gerencie suas configurações do Centro de administração do Office 365 a partir da linha de comando. Conectar-se ao Office 365 PowerShell é um processo simples de três etapas em que você instala o software necessário, executa-o e, em seguida, conecta-se à sua organização do Office 365. Observe que essas instruções de conexão são as mesmas do tópico Gerenciar o Azure AD usando o Windows PowerShell.</p>
<ol>
<li style="text-align: justify;"><strong>Etapa 1: Instalar o software necessário</strong><br />
Essas etapas precisam ser executadas apenas uma vez em seu computador e não toda vez em que você se conectar. No entanto, você provavelmente precisará instalar a versão mais recente do software periodicamente.<br />
Instale a versão de 64 bits do Assistente de Conexão do Microsoft Online Services: Assistente de Conexão do Microsoft Online Services para Profissionais de TI RTW.<br />
Instalar a versão de 64 bits do Módulo Microsoft Azure Active Directory para Windows PowerShell: Módulo Microsoft Azure Active Directory para Windows PowerShell (versão de 64 bits).</li>
<li><strong>Etapa 2: Abrir o Módulo do Microsoft Azure Active Directory</strong><br />
Localizar e abrir o Módulo Microsoft Azure Active Directory para Windows PowerShell usando um dos seguintes métodos com base na sua versão do Windows:<br />
No menu <strong>Iniciar</strong>, insira <strong>Azure</strong> na caixa <strong>Pesquisar</strong> programas e arquivos.<br />
Nos resultados, escolha Módulo Microsoft Azure Active Directory para Windows PowerShell.</li>
</ol>
<p><strong>Conectar-se à assinatura do Office 365</strong></p>
<p>No Módulo Microsoft Azure Active Directory para Windows PowerShell, execute o seguinte comando.</p>
<blockquote><p>
$UserCredential = Get-Credential</p></blockquote>
<p>Na caixa de diálogo Solicitação de Credencial do Windows PowerShell, digite o nome de usuário e a senha do Office 365conta comercial ou escolar e clique em OK.<br />
Execute o comando a seguir.</p>
<blockquote><p>
Connect-MsolService -Credential $UserCredential</p></blockquote>
