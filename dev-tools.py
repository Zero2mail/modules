


def register(cb):
	cb(AudioEditorMod())
class AudioEditorMod(loader.Module):
	"""AudioEditor"""
	strings = {'name': 'AudioEditor'}


event.edit(f"ID Чата: {event.chat_id}")
