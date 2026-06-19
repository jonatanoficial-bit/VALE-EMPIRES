from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
THEME = 'assets/audio/music/vale-empires-official-theme.mp3'


def test_official_theme_exists_and_is_not_empty():
    p = ROOT / THEME
    assert p.exists()
    assert p.stat().st_size > 1_000_000


def test_audio_engine_uses_official_theme_for_main_music():
    js = (ROOT / 'js/audio-engine.js').read_text(encoding='utf-8')
    assert "const OFFICIAL_THEME='assets/audio/music/vale-empires-official-theme.mp3'" in js
    assert 'menu:OFFICIAL_THEME' in js
    assert 'exploration:OFFICIAL_THEME' in js
    assert 'combat:OFFICIAL_THEME' in js
    assert 'activePath.endsWith(path)' in js


def test_audio_manifest_registers_official_theme():
    manifest = json.loads((ROOT / 'assets/audio/audio-manifest.json').read_text(encoding='utf-8'))
    assert manifest['music']['menu'] == THEME
    assert manifest['music']['exploration'] == THEME
    assert manifest['music']['combat'] == THEME
    assert manifest['officialTheme']['durationSeconds'] == 152.904


def test_service_worker_precaches_theme_and_bumps_cache():
    sw = (ROOT / 'service-worker.js').read_text(encoding='utf-8')
    assert 'vale-empires-v4.13.0-f47-official-theme-audio' in sw
    assert './assets/audio/music/vale-empires-official-theme.mp3' in sw


def test_build_metadata_phase_47_preserves_schema():
    build = json.loads((ROOT / 'BUILD.json').read_text(encoding='utf-8'))
    assert build['version'] == 'v4.13.0'
    assert build['phase'] == '47'
    assert build['saveSchema'] == 26
    assert build['audioAsset']['file'] == THEME
