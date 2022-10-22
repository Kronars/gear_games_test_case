import pytest
from time import sleep
from altunityrunner import By


def test_volume_changing(scene_main, driver_conn):
    '''Тест изменения громкости'''
    driver_conn.find_object(By.NAME, 'SettingButton').tap()

    settings_path = '//UICamera/Loadout/SettingPopup/Background/'

    master_vol = driver_conn.find_object(By.PATH, settings_path+'MasterSlider')
    music_vol  = driver_conn.find_object(By.PATH, settings_path+'MusicSlider')
    sfx_vol    = driver_conn.find_object(By.PATH, settings_path+'MasterSFXSlider')

    driver_conn.swipe(*master_vol.get_screen_position(), int(master_vol.x) - 200, master_vol.y, duration_in_secs=1)
    driver_conn.swipe(*music_vol.get_screen_position(), int(master_vol.x) - 200, master_vol.y, duration_in_secs=1)
    driver_conn.swipe(*sfx_vol.get_screen_position(), int(master_vol.x) - 200, master_vol.y, duration_in_secs=1)
    sleep(1)
    assert master_vol.get_component_property('UnityEngine.UI.Slider', 'value') == '0.0'
    assert music_vol.get_component_property('UnityEngine.UI.Slider', 'value') == '0.0'
    assert sfx_vol.get_component_property('UnityEngine.UI.Slider', 'value') == '0.0'


@pytest.mark.parametrize(
    "page_name,expected",
    [
        ('Item', ['Magnet', 'x2', 'Invincible', 'Life',]),
        ('Character', ['Trash Cat', 'Rubbish Raccoon']),
        ('Accesories', ['Safety', 'Party Hat', 'Smart', 'Safety', 'Party Hat',]),
        ('Themes', ['Day', 'NightTime',]),
    ]
)
def test_shop_items(page_name, expected, scene_shop, driver_conn):
    '''Параметрезированный тест наличия предметов в разделах в магазина'''

    driver_conn.find_object(1, page_name).tap()
    shop_items = driver_conn.find_objects(1, 'ItemEntry(Clone)')

    for item in shop_items:
        item = driver_conn.find_object(By.PATH, f'//@id={item.id}/NamePriceButtonZone/Name')
        item_name = item.get_component_property('UnityEngine.UI.Text', 'text')

        assert item_name in expected


def test_death_sequence(scene_main, driver_conn):
    '''Тест наличия всех элементов интерефейса после смерти'''
    driver_conn.find_object(1, 'StartButton').tap()
    # Опасно и медленно, но реализация управления персонажем заняла слишком многоо времени 
    death = driver_conn.wait_for_object(By.NAME, 'DeathPopup', timeout=40)

    elements = driver_conn.find_objects(By.PATH, f'//@id={death.id}/*')
    elements_names = [el.name for el in elements]

    assert set(['Text', 'ButtonLayout', 'PremiumDisplay', 'GameOver']) == set(elements_names)

    driver_conn.find_object(1, 'GameOver').tap()

    elements = driver_conn.find_objects(By.PATH, f'//GameOver/*')
    elements_names = [el.name for el in elements]
    
    assert set(elements_names) == set(['Text','Highscore','OpenLeaderboard','Loadout','RunButton','MissionsButton','StoreButton'])
