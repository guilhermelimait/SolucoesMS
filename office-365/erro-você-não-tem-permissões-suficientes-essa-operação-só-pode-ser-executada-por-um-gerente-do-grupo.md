# Erro: Você não tem permissões suficientes. Essa operação só pode ser executada por um gerente do grupo

Date: 2018-07-31 17:14:45

Categories: Exchange, Office 365

---

<p>Um erro meio estranho apareceu ao mudar o proprietário de uma lista no O365, para isso, algumas razões podem se aplicar;</p>
<p><strong>Erro: </strong></p>
<p>Você não tem permissões suficientes. Essa operação só pode ser executada por um gerente do grupo</p>
<p><strong>Causas: </strong></p>
<p>Depois da transição do BPOS para Office 365 a Lista de Distribuição não possui &#8220;proprietário&#8221;.</p>
<p>O administrador original o qual criou a Lista de Distribuição não existe no Dominio.</p>
<p>O administrador atual não possui as permissões necessárias para editar a Lista.</p>
<p>Quando um usuário possui a função de administrador &#8220;Security Group Creation and Membership&#8221; no Gerenciador do Exchange Online, mas não pode modificar a Lista de Distribuição.</p>
<p><strong>Solução:</strong></p>
<p>Para resolver este problema conecte o seu PowerShell e execute os seguintes comandos.</p>
<p><strong>Para dar permissão de Proprietário de uma lista de Distribuição</strong></p>
<p>Set-DistributionGroup &#8220;Nome do Grupo&#8221; -ManagedBy &#8220;Admin@contoso.com&#8221; –BypassSecurityGroupManagerCheck</p>
<p><strong>Para adicionar membros a Lista de Distribuição</strong></p>
<p>Add-DistributionGroupMember –Identity &#8220;Nome do Grupo&#8221; –Member user@contoso.com</p>
<p><strong>Para remover um membro de uma Lista de Distribuição</strong></p>
<p>Remove-DistributionGroupMember -Identity &#8220;Nome do Grupo&#8221; -Member user@contoso.com</p>
<p><strong>Para verificar membros de uma Lista de Distribuição</strong></p>
<p>Get-DistributionGroupMember -identity &#8220;Nome do Grupo&#8221;|fl DisplayName,WindowsLiveID,RecipientType</p>
<p>Enjoy!</p>
<p>Fonte: <a href="https://solucoesoffice365.wordpress.com/2012/03/26/erro-quando-tenta-adicionar-modificar-ou-remover-usurios-em-uma-lista-de-distribuio-no-office-365/">SolucoesOffice365</a></p>
