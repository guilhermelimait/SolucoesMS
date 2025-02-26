# Como criar uma função Random usando Texto no PowerApps?

Date: 2021-06-17 15:43:08

Categories: O365, Office 365, PowerApps

---

<p>Em um novo projeto, eu gostaria de criar um &#8220;Olá mundo&#8221; em várias linguas, e para isso, precisava de uma função randômica para que sempre que o form fosse apresentado, uma nova mensagem fosse apresentada. Para isso, utilizei de um conjunto de funções, onde o resultado transformou no que eu precisava, veja só:</p>
<p>1 &#8211; No objeto <strong>Screen</strong>, função <strong>OnVisible</strong> crie a fórmula:</p>
<p><em>  UpdateContext({HelloWord:First(Shuffle([&#8220;Ni hao&#8221;, &#8220;Ciao&#8221;, &#8220;Hello&#8221;, &#8220;Holla&#8221;])).Value})</em></p>
<p>2- Crie um <strong>Label</strong>, na função <strong>Text</strong> crie a fórmula:</p>
<p><em>  HelloWord &amp; &#8221; &#8221; &amp; Office365Users.MyProfile().GivenName &amp; &#8220;!&#8221;</em></p>
<p>Nesse exemplo, estou usando também o conector do O365 para mostrar o nome do usuário.</p>
<p>Enjoy!</p>
