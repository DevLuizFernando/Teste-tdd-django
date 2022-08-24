from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--remote-debugging-port=9222")
        self.browser = webdriver.Chrome('/Users/User/Desktop/desktop/tdd_busca_animal/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'sim',
            venenoso = 'não',
            domestico = 'não'
        )

    def tearDown(self) -> None:
        self.browser.quit()

    

    def test_buscando_um_novo_animal(self):
        """Teste se um usuário encontra um animal na pesquisa"""
        # Vini, deseja encontrar um novo animal,
        # para adotar.

        
        # Ele encontra o Busca animal e decide usar o sit, 
        home_page = self.browser.get(self.live_server_url + '/')
       
        # porque ele vê no menu do site escrito Busca animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')
       
        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        
        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um leão.
        