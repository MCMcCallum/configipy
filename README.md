# config
A small library to assist with creating classes that are configurable via yaml files.

Sometimes it's just easier to read a yaml file for an experiment configuration than searchig through code.

The idea is to have a light wrapper around loading yaml files into dictionaries, and an interface for classes whose attributes are set by these yaml dictionaries.

For example a configuration object is created via:

```
from config import Config

cfg = Config('v0.0')
```

where "v0.0" exists at the end of the filename of the desired yaml file.

Configurable objects are a subclass of the Configurable class:

```
from config import Configurable
from config import Config

class ConfigurableSubclass(Configurable):

	def PrintBatchSize(self):
		print(str(self._batch_size))

cfg = Config('v0.0')

example = ConfigurableSubclass(cfg['experiment_config'])
example.PrintBatchSize()
```

Should output `128`.
